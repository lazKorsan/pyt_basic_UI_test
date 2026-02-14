Feature: Kullanıcı promotion oluşturur
  @promotion
  Scenario: instructor kullanıcısı promotion oluşturur
    Given Kullanıcı giriş sayfasını açar
    When instuLearn kullanıcısı admin giriş yapar
    When instulearn kullanıcısı promotion oluşturur
