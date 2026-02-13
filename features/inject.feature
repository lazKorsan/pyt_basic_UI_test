Feature: Kullanici multiple data import eder
@inject
  Scenario: Kullanici testdata , pages siniflarindan bilgi injeciton eder
    Given Kullanici  "instuLearn" sayfasina gider
    When Kullanici instructor kullanici girisini secer
    Then Kullanici "