Feature: Google Ana Sayfa Erişimi

  @smoke
  Scenario: Google ana sayfasını başarıyla açma
    Given Kullanıcı tarayıcıyı açar
    When Kullanıcı "https://www.google.com" adresine gider
    Then Sayfa başlığının "Google" içerdiğini doğrular