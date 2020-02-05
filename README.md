# Teste de conexão python-metatrader5
<p>
 Script para teste de conexão entre python e metatrader5. 
</p>

<p>
Esse script tem como base o script disponibilizado na documentação do metatrader5, segue link:
https://www.mql5.com/pt/docs/integration/python_metatrader5
</p>
<p>
Como o metatrader foi desenvolvido para o mercado forex, para usarmos essa nova integração no mercado nacional, é necessário algumas pequenas mudanças. Segue uma sugestão para a aquisição de dados direto do metatrader.
</p>
<p>
Os primeiros resultados impresso são tuplas, eles dizem respeito a sua conexão e a sua conta, vale a pena consultar a documentação para
entender melhor cada uma das saídas.

![res1](https://user-images.githubusercontent.com/24875841/73802756-5e8da480-479d-11ea-849b-1945a5e75ecb.PNG)
</p>
<p>
Os próximos resultados impresso são do minicontrato futuro de índice (WIN), depois os minicontratos de dólar (WDO), PETR4, RADL3 e por fim o IBOV.

![res2](https://user-images.githubusercontent.com/24875841/73803140-a3fea180-479e-11ea-81f1-36ff2b46ea8f.PNG)

![res3](https://user-images.githubusercontent.com/24875841/73803550-da88ec00-479f-11ea-808a-7c8948b47a97.PNG)

![petr4](https://user-images.githubusercontent.com/24875841/73803605-1623b600-47a0-11ea-8830-ddc33c88db98.PNG)

![radl3](https://user-images.githubusercontent.com/24875841/73803628-263b9580-47a0-11ea-9708-dd6f6a291e5a.PNG)

![ibov](https://user-images.githubusercontent.com/24875841/73803649-33f11b00-47a0-11ea-93d2-42e5afd9a13e.PNG)
</p>
<p>
O gráfico plotado do bid e ask do minicontrato de índice será o seguinte:

![grafico-bid-ask](https://user-images.githubusercontent.com/24875841/73803793-977b4880-47a0-11ea-8cb4-b69b7a15279a.PNG)
</p>
