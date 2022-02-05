# feature - + анатация из ррех строк
# Короткое, но исчерпывающее описание требуемого функционала
# функциональность приложения Scenario - само название сценария Given - дано  When -
#это файл характеристик


Feature: Login and check amount

    Scenario Outline: Check profile user
        Given Log in as a specific user "<name>"
        When Сleanup of gaps in database data <id> <amount> <username>
        Then Equal number of tables <amount>


    Examples: test
    |  id  |  amount |  username |       name       |
    |  1   |   233   |   helen   | Hermoine Granger |
    |  2   |    34   |   elena   |                  |