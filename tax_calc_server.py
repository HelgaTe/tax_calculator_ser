import streamlit as st
import pandas as pd


# Server application for tax calculator

def calculate_taxes(base_salary_expensify, bonus, insurance):
    total_compensation = base_salary_expensify + bonus + insurance
    single_tax = total_compensation * 0.05
    military_tax = total_compensation * 0.01
    social_tax = 45  # фіксована сума
    total_taxes = single_tax + military_tax + social_tax

    return total_compensation, single_tax, social_tax, total_taxes
    # military tax is temporarily deactivated (add to <return> for activation)


# Заголовок програми
st.title("Калькулятор податків")

# Вибір місяця
month = st.selectbox("Місяць", [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
])

# Введення даних
base_salary = st.number_input("Base Salary (expensify incl.)", min_value=0.0, step=1.0)
bonus = st.number_input("Bonus", min_value=0.0, step=1.0)
insurance = st.number_input("Insurance", min_value=0.0, step=1.0)

# Кнопка розрахунку
if st.button("Розрахувати"):
    # total_compensation, single_tax, military_tax, social_tax, total_taxes = calculate_taxes(
    #     base_salary, bonus, expensify, insurance
    # )
    total_compensation, single_tax, social_tax, total_taxes = calculate_taxes(
        base_salary, bonus, insurance
    )  # military tax is temporarily deactivated

    # Вивід результатів
    st.subheader("Результати")
    st.write(f"Місяць: {month}")  # Виведення вибраного місяця
    st.write(f"Загальна компенсація: {total_compensation:.2f} $")
    st.write(f"Єдиний податок (5%): {single_tax:.2f} $")
    # st.write(f"Військовий збір (1%): {military_tax:.2f} $")  # military tax is temporarily deactivated
    st.write(f"ЄСВ (місячний платіж): {social_tax:.2f} $")
    st.write(f"Сума для сплати податків: {total_taxes:.2f} $")

    # Збереження в Excel
    results = {
        "Category": ["Base salary (expensify incl.)", "Bonus", "Insurance", "Total Compensation",
                     "Single Tax (5%)", "Social Tax (monthly payment)", "Total Taxes"],
        "Amount, $": [base_salary, bonus, insurance, total_compensation,
                       single_tax, social_tax, total_taxes]
    }  # military tax is temporarily deactivated
    results_df = pd.DataFrame(results)

    # results = {
    #     "Category": ["Base Salary", "Bonus", "Expensify", "Insurance", "Total Compensation",
    #                  "Single Tax (5%)", "Military Tax (1%)", "Social Tax (fixed)", "Total Taxes"],
    #     "Amount ($)": [base_salary, bonus, expensify, insurance, total_compensation,
    #                    single_tax, military_tax, social_tax, total_taxes]
    # }
    # results_df = pd.DataFrame(results)

    @st.cache_data
    @st.cache_data
    def convert_df_to_excel(df):
        from io import BytesIO
        output = BytesIO()

        # Використовуємо pd.ExcelWriter з xlsxwriter
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False, sheet_name="Tax Results")

            # Отримуємо об'єкт workbook і worksheet для форматування
            workbook = writer.book
            worksheet = writer.sheets["Tax Results"]

            # Створюємо формат для жирного шрифту
            bold_format = workbook.add_format({"bold": True})

            # Застосовуємо жирний шрифт
            worksheet.set_row(4, None, bold_format)  # A5 cell
            worksheet.set_row(7, None, bold_format)  # A8 cell

            # Автоматично розширюємо ширину стовпця "Category" (стовпець A)
            max_width = max(df["Category"].str.len()) + 2  # Додаємо запас у 2 символи
            worksheet.set_column("A:A", max_width)
            worksheet.set_column("B:B", max_width)


        return output.getvalue()


    excel_data = convert_df_to_excel(results_df)
    st.download_button(
        label="Завантажити результати в Excel",
        data=excel_data,
        file_name=f"tax_results_{month}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
