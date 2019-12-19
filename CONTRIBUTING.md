## Fluxo de desenvolvimento

### Convenções

1. Caso for trabalhar em um bugfix, utilize '**-fix**' como sufixo. Exemplo: -queue-**fix**

### Regras

1. Sempre
  * Desenvolva apenas em seu branch.
  * Faça rebase com o **master** **antes** de criar _pull requests_.
  * Se esforce para manter o **master** o mais limpo possível.
  * Faça rebase do **master** em seu branch diariamente.
  * Faça commits pequenos, que descrevem alterações únicas. (Leia: [Commit Guidelines](https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project#Commit-Guidelines))
  * Faça squash dos seus commits que não estão completos (_Work In Progress_)
2. Nunca
  * Desenvolva direto no **master**.
  * Faça merge de branches no **master** antes que o código seja revisado.
  * Revise _pull requests_ que:
    * Não estejam atualizados com o **master**.
    * Tenham testes quebrando.

### Processos
#### Desenvolvimento

Este processo vale tanto para bugfixes quanto para novas funcionalidades.

1. Clone do **master**: ```git clone https://gitlab.luizalabs.com/luizalabs/projeto```
2. Crie seu branch:
  * ```git checkout -b dg-queue```
4. Enquanto estiver desenvolvendo
  * Diariamente:
    * ```git checkout master```
    * ```git pull origin master```
    * ```git checkout dg-queue```
    * ```git rebase master```
  * Eventualmente - possivelmente mais de 1 vez por dia: ```git push origin dg-queue```
5. Após terminar o desenvolvimento
  * Disponibilize seu branch para teste da funcionalidade - seja em um sandbox ou no ambiente local. Se a funcionalidade não for validada, volte ao passo 4.
  * Conserte os testes que estiverem falhando.
  * Atualize o versionamento do projeto (no padrão de [versionamento semântico](http://semver.org/lang/pt-BR/spec/v2.0.0.html)).
  * Preencha o **CHANGELOG.md** com as alterações realizadas em seu _branch_.
  * Faça push do seu branch para o repositório: ```git push --force origin dg-queue```
  * Crie o pull request.
  * Notifique sua equipe que o pull request foi criado.
  * Interaja com o revisor de seu pull request quantas vezes forem necessárias.
  * Após o Pull Request aprovado:
    * Considere fazer squash de alterações pontuais que tenham sido feitas durante a revisão.
    * Faça rebase com o master, caso seu _branch_ esteja desatualizado.

#### Revisão

Guidelines:

1. Seja duro (mas gentil), fará bem a todos: não faça revisões caso as regras descritas acima não tenham sido cumpridas. Se não forem, avise o desenvolvedor para que ele possa cumprir os requisitos e atualizar o branch dele - um novo merge request pode não ser necessário.
2. Se você não entender o código que está lendo, pergunte. Faça perguntas mesmo que achar ou tiver certeza que elas são ingênuas ou simples demais, esse comportamento trará transparência e incentiva os outros desenvolvedores a agir da mesma forma - os encorajam a perguntar sempre que tiverem dúvidas.
3. Sugira melhorias, use o bom senso.
4. Se o merge request for claramente ruim, recuse.
5. Exclua o _branch_ após realizar o merge dele no _master_.

#### Changelog

* Escreva o changelog como se estivesse descrevendo quais mudanças foram introduzidas no _release_ para um colega de time.

#### Úteis

* Alias para rodar ```git lg``` com log colorido e com níveis de merge/branches explícitos:
  * ```git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"```

### Padrões
#### Lint

Siga sempre os padrões e boas práticas já consagradas da comunidade Python, algumas ferramentas podem lhe auxiliar nisso (e.g. Flake8, PyLint, MyPy, etc.).
O comando `make lint` já fara as verificações necessárias para que seu código entregue o minimo desses padrões.

#### Estrutura de diretórios

Alguns diretórios são diretórios chave para a organização do projeto:

* **settings**: configurações gerais de funcionamento do projeto. É neste diretório que as configurações de teste, sandbox, produção, etc, estão organizados.
* **backend**: interfaces, abstrações genéricas e backends pools. É recomendavel que integrações ou mecanismos que podem mudar sejam desenvolvidos através de interfaces e as implementações concretas sejam escritas de forma separada, assim é possível por exemplo escrever um backend que faça uma integração com uma API de terceiros e escrever uma versão fake desse backend, facilitando assim os testes e possiveis alterações (e.g. passar a usar outra API de terceiro com pouca mudança de código).
* **extensions**: extensões do projeto. As implementações concretas dos backends devem ficar nesse diretório por exemplo.
* **contrib**: ferramentas e facilitadores que não possuem regras de negócio. Seguindo a filosofia do Python de "baterias inclusas", usamos o contrib para adicionar as baterias que faltam na linguagem ou nos frameworks utilizados no projeto.


### Recomendações
#### Teste
* Se esforce para manter a cobertura de testes compativel com o valor atual do master.
* Não escreva testes unitários que dependam de acesso a internet (e.g. testes de integração com APIs de terceiro), prefira escrever utilizando mocks.
* Sempre que possível, escreva testes de integração que façam **requisições reais** aos sistemas dependentes,
porém, esses testes devem possuir uma receita propria para serem executados (i.e. não serem executados na stack de testes unitários).
* Use storages reais no ambiente de testes do _CI_ para evitar diferenças de comportamento entre implementações _InMemory_ VS _ConcretStorage_ (e.g. sqlite vs MySql).

#### Python
* Use somente coroutines nativas (`async def` / `await`) e não coroutines com a syntax antiga (`@asyncio.coroutine` / `yield from`)
