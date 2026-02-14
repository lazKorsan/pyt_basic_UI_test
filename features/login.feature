Feature: Kullanıcı Giriş Testleri
  Sistemdeki farklı kullanıcı hesapları ve şifre kombinasyonları ile
  giriş fonksiyonelliğinin doğrulanması.
@login
  Scenario Outline: Çoklu kullanıcı bilgileri ile giriş denemesi
    Given Kullanıcı giriş sayfasını açar
    When Kullanıcı "<mail>" ve "<password>" bilgilerini girer
    Then Giriş işleminin gerçekleştiği doğrulanır

    Examples: Veri Seti
      | mail                                | password   |
      | lazKorsan20260213072041@gmail.com   | Query.2026 |
      | lazKorsan@gmail.com                 | Query.2026 |
      | lazKorsan20260213072041@gmail.com   | Query.2025 |
