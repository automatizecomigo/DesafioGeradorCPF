from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect, Page

scenarios('../feature/gerador_cpf.feature')

cpf_gerado = "7"


@given("que estou na pagina de geracao de CPF")
def pagina_inicial_de_gerador_cpf(browser: Page):
    browser.goto('https://www.4devs.com.br/gerador_de_cpf', timeout=170000)


@when("marco a opcao para nao gerar pontuacao")
def seleciono_a_opcao_nao(browser: Page):
    browser.locator('[id="pontuacao_nao"]').click()


@when('escolho o estado de origem com "AM" e clico no botao "GERAR CPF"')
def escolho_o_estado_AM_e_clico_no_botao_para_gerar_o_CPF(browser: Page):
    browser.locator('[name="cpf_estado"]').click()
    browser.locator("#cpf_estado").select_option("AM")
    browser.locator('[type="button"]').click()

    button_locator = browser.locator('[type="button"]')

    while True:
        button_locator.click()
        if cpf_gerado and cpf_gerado.startswith('7'):
         break


@then('o CPF gerado deve comecar com "7"')
def valido_se_o_primeiro_digito_e_7(browser: Page):
    expect(browser.get_by_text('7'))

