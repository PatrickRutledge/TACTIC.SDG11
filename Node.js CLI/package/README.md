wxflows
=================

IBM watsonx Flows Engine CLI

[![oclif](https://img.shields.io/badge/cli-oclif-brightgreen.svg)](https://oclif.io)
[![Version](https://img.shields.io/npm/v/wxflows.svg)](https://npmjs.org/package/wxflows)
[![Downloads/week](https://img.shields.io/npm/dw/wxflows.svg)](https://npmjs.org/package/wxflows)

<!-- toc -->
* [Usage](#usage)
* [Commands](#commands)
<!-- tocstop -->

# Usage

<!-- usage -->
```sh-session
$ npm install -g wxflows
$ wxflows COMMAND
running command...
$ wxflows (--version|-v)
wxflows/2.0.0 linux-x64 node-v22.13.1
$ wxflows --help [COMMAND]
USAGE
  $ wxflows COMMAND
...
```
<!-- usagestop -->

# Commands

<!-- commands -->
* [`wxflows deploy`](#wxflows-deploy)
* [`wxflows help [COMMAND]`](#wxflows-help-command)
* [`wxflows import [SOURCE]`](#wxflows-import-source)
* [`wxflows import curl`](#wxflows-import-curl)
* [`wxflows import db2 [JDBCURL]`](#wxflows-import-db2-jdbcurl)
* [`wxflows import flow [FLOW]`](#wxflows-import-flow-flow)
* [`wxflows import graphql [URL]`](#wxflows-import-graphql-url)
* [`wxflows import mysql [DSN]`](#wxflows-import-mysql-dsn)
* [`wxflows import oracle [JDBCURL]`](#wxflows-import-oracle-jdbcurl)
* [`wxflows import postgresql [DSN]`](#wxflows-import-postgresql-dsn)
* [`wxflows import snowflake [DSN]`](#wxflows-import-snowflake-dsn)
* [`wxflows import tool URI`](#wxflows-import-tool-uri)
* [`wxflows init`](#wxflows-init)
* [`wxflows login [DOMAIN]`](#wxflows-login-domain)
* [`wxflows logout`](#wxflows-logout)
* [`wxflows tools`](#wxflows-tools)
* [`wxflows tools list`](#wxflows-tools-list)
* [`wxflows tools ls`](#wxflows-tools-ls)
* [`wxflows whoami`](#wxflows-whoami)

## `wxflows deploy`

Deploy to Flows Engine.

```
USAGE
  $ wxflows deploy [-h] [--non-interactive] [--dir DIRECTORY]

FLAGS
  -h, --help             Show CLI help
      --dir=DIRECTORY    Working directory [default: current directory]
      --non-interactive  Disable all interactive prompts

DESCRIPTION
  Deploy to Flows Engine.
```

## `wxflows help [COMMAND]`

Display help for wxflows.

```
USAGE
  $ wxflows help [COMMAND...] [-n]

ARGUMENTS
  COMMAND...  Command to show help for.

FLAGS
  -n, --nested-commands  Include all nested commands in the output.

DESCRIPTION
  Display help for wxflows.
```

_See code: [@oclif/plugin-help](https://github.com/oclif/plugin-help/blob/v6.2.18/src/commands/help.ts)_

## `wxflows import [SOURCE]`

Import a schema for an external data source or an API endpoint into your GraphQL API.

```
USAGE
  $ wxflows import [SOURCE...] [-h] [--non-interactive] [--dir <value>]

ARGUMENTS
  SOURCE...  kind of the data source: curl, graphql, mysql, postgresql, snowflake, db2, oracle (or a full DSN string)

FLAGS
  -h, --help             Show CLI help
      --dir=<value>      Working directory
      --non-interactive  Disable all interactive prompts

DESCRIPTION
  Import a schema for an external data source or an API endpoint into your GraphQL API.
  See more details with wxflows import [SOURCE] --help
```

## `wxflows import curl`

Import a schema for a REST endpoint into your GraphQL API (uses the curl syntax).

```
USAGE
  $ wxflows import curl [-h] [--non-interactive] [--dir <value>] [--name <value>] [--prefix <value>] [-H
    <value>...] [--header-param <value>...] [--query-name <value>] [--query-type <value>] [--path-params <value>]

FLAGS
  -H, --header=<value>...
      Specifies a request header to pass

      Example:
      stepzen import curl https://example.com/api/customers \
      -H "Authorization: apikey SecretAPIKeyValue"

  -h, --help
      Show CLI help

  --dir=<value>
      Working directory

  --header-param=<value>...
      Specifies a parameter in a header value. Can be formed by taking a -H, --header flag and replacing the variable part
      of the header value with a $paramName placeholder. Repeat this flag once for each header with a parameter.

      Example:
      stepzen import curl https://example.com/api/customers \
      -H "Authorization: apikey SecretAPIKeyValue" \
      --header-param 'Authorization: apikey $apikey'

  --name=<value>
      Subfolder inside the workspace folder to save the imported schema files to. Defaults to the name of the imported
      schema.

  --non-interactive
      Disable all interactive prompts

  --path-params=<value>
      Specifies path parameters in the URL path. Can be formed by taking the original path and replacing the variable
      segments with $paramName placeholders.

      Example:
      stepzen import curl https://example.com/users/jane/posts/12 --path-params '/users/$userId/posts/$postId'

  --prefix=<value>
      Prefix to add to every type in the generated schema

  --query-name=<value>
      Property name to add to the Query type as a way to access the imported endpoint

  --query-type=<value>
      Name for the type returned by the curl request in the generated schema. The name specified by --query-type is not
      prefixed by --prefix if both flags are present.

DESCRIPTION
  Import a schema for a REST endpoint into your GraphQL API (uses the curl syntax).

  wxflows import curl automatically introspects a REST endpoint, generates a GraphQL schema for accessing this endpoint
  through a Flows Engine API, and adds the generated types and a query field into your GraphQL schema.
```

## `wxflows import db2 [JDBCURL]`

Import a schema for a Db2 data source into your GraphQL API.

```
USAGE
  $ wxflows import db2 [JDBCURL...] [-h] [--non-interactive] [--dir <value>] [--name <value>] [--db-schema
    <value>] [--db-link-types] [--db-include tables-only|views-only|tables-and-views] [--db-use-deprecated-2022-naming]

ARGUMENTS
  JDBCURL...  (optional) JDBC URL of a Db2 database.
              Example: 'jdbc:db2://host:port/db:user=username;password=password;schema=schema;sslConnection=true/false;'

              The --db-schema flag overrides the schema part of the JDBC URL (if both are provided).

FLAGS
  -h, --help
      Show CLI help

  --db-include=<option>
      Should the generated GraphQL schema be based only on database views, only on tables or on both
      <options: tables-only|views-only|tables-and-views>

  --db-link-types
      Automatically link types based on foreign key relationships using @materializer
      (https://stepzen.com/docs/features/linking-types)

  --db-schema=<value>
      Database schema to import tables from (default: public)

  --db-use-deprecated-2022-naming
      Use the deprecated pre-2023 naming convention in the generated GraphQL schema:
      - the generated type and property names are auto-capitalized into PascalCase
      - the generated field names use the getCustomer and getCustomerList style.

      On the other hand, when using the default naming convention:
      - the generated type and property names match exactly the DB table and column names
      - the generated field names use the customer and customerList style.

  --dir=<value>
      Working directory

  --name=<value>
      Subfolder inside the workspace folder to save the imported schema files to. Defaults to the name of the imported
      schema.

  --non-interactive
      Disable all interactive prompts

DESCRIPTION
  Import a schema for a Db2 data source into your GraphQL API.

  wxflows import db2 automatically introspects a Db2 database, generates a GraphQL schema for accessing this database
  through a Flows Engine API, and merges the generated types, queries and mutations into your GraphQL schema.
```

## `wxflows import flow [FLOW]`

Import Flows Engine flow expression as a query field into your GraphQL API.

```
USAGE
  $ wxflows import flow [FLOW...] [-h] [--non-interactive] [--dir <value>] [--name <value>] [-H <value>...
    --endpoint <value>]

FLAGS
  -H, --header=<value>...  Specifies a request header to pass

                           Example:
                           stepzen import curl https://example.com/api/customers \
                           -H "Authorization: apikey SecretAPIKeyValue"
  -h, --help               Show CLI help
      --dir=<value>        Working directory
      --endpoint=<value>   Use a custom GraphQL schema instead of the project's schema as the schema providing the steps
                           in the flow.
      --name=<value>       Subfolder inside the workspace folder to save the imported schema files to. Defaults to the
                           name of the imported schema.
      --non-interactive    Disable all interactive prompts

DESCRIPTION
  Import Flows Engine flow expression as a query field into your GraphQL API.

  wxflows import flow automatically introspects a GraphQL endpoint and adds a @sequence implementing the given flow
  expression into your GraphQL schema.
```

## `wxflows import graphql [URL]`

Import a GraphQL API as a subgraph into your GraphQL API.

```
USAGE
  $ wxflows import graphql [URL...] [-h] [--non-interactive] [--dir <value>] [--name <value>] [--prefix <value>] [-H
    <value>...] [--header-param <value>...]

FLAGS
  -H, --header=<value>...
      Specifies a request header to pass

      Example:
      stepzen import curl https://example.com/api/customers \
      -H "Authorization: apikey SecretAPIKeyValue"

  -h, --help
      Show CLI help

  --dir=<value>
      Working directory

  --header-param=<value>...
      Specifies a parameter in a header value. Can be formed by taking a -H, --header flag and replacing the variable part
      of the header value with a $paramName placeholder. Repeat this flag once for each header with a parameter.

      Example:
      stepzen import curl https://example.com/api/customers \
      -H "Authorization: apikey SecretAPIKeyValue" \
      --header-param 'Authorization: apikey $apikey'

  --name=<value>
      Subfolder inside the workspace folder to save the imported schema files to. Defaults to the name of the imported
      schema.

  --non-interactive
      Disable all interactive prompts

  --prefix=<value>
      Prefix to add to every type in the generated schema

DESCRIPTION
  Import a GraphQL API as a subgraph into your GraphQL API.

  wxflows import graphql automatically introspects a GraphQL endpoint and merges the types, queries, mutations and
  subscriptions for accessing this endpoint through a Flows Engine API into your GraphQL schema.
```

## `wxflows import mysql [DSN]`

Import a schema for a MySQL data source into your GraphQL API.

```
USAGE
  $ wxflows import mysql [DSN...] [-h] [--non-interactive] [--dir <value>] [--name <value>] [--db-host <value>]
    [--db-user <value>] [--db-password <value>] [--db-database <value>] [--db-link-types] [--db-include
    tables-only|views-only|tables-and-views] [--db-use-deprecated-2022-naming]

ARGUMENTS
  DSN...  (optional) Data Source Name (DSN) of a MySQL database.
          Example: mysql://user:password@host:port/database

          Flags, such as --db-host, override the corresponding parts of the DSN (if both are provided).

FLAGS
  -h, --help
      Show CLI help

  --db-database=<value>
      Name of database to import

  --db-host=<value>
      Database host and optional port (as HOST[:PORT])

  --db-include=<option>
      Should the generated GraphQL schema be based only on database views, only on tables or on both
      <options: tables-only|views-only|tables-and-views>

  --db-link-types
      Automatically link types based on foreign key relationships using @materializer
      (https://stepzen.com/docs/features/linking-types)

  --db-password=<value>
      Database password

  --db-use-deprecated-2022-naming
      Use the deprecated pre-2023 naming convention in the generated GraphQL schema:
      - the generated type and property names are auto-capitalized into PascalCase
      - the generated field names use the getCustomer and getCustomerList style.

      On the other hand, when using the default naming convention:
      - the generated type and property names match exactly the DB table and column names
      - the generated field names use the customer and customerList style.

  --db-user=<value>
      Database user name

  --dir=<value>
      Working directory

  --name=<value>
      Subfolder inside the workspace folder to save the imported schema files to. Defaults to the name of the imported
      schema.

  --non-interactive
      Disable all interactive prompts

DESCRIPTION
  Import a schema for a MySQL data source into your GraphQL API.

  wxflows import mysql automatically introspects a MySQL database, generates a GraphQL schema for accessing this
  database through a Flows Engine API, and merges the generated types, queries and mutations into your into your GraphQL
  schema.
```

## `wxflows import oracle [JDBCURL]`

Import a schema for a oracle data source into your GraphQL API.

```
USAGE
  $ wxflows import oracle [JDBCURL...] [-h] [--non-interactive] [--dir <value>] [--name <value>] [--db-schema
    <value>] [--db-link-types] [--db-include tables-only|views-only|tables-and-views] [--db-use-deprecated-2022-naming]

ARGUMENTS
  JDBCURL...  (optional) JDBC URL of an Oracle database.
              Example: 'jdbc:oracle:thin:user/password@//host:port/db?currentschema=schema'

              The --db-schema flag overrides the schema part of the JDBC URL (if both are provided).

FLAGS
  -h, --help
      Show CLI help

  --db-include=<option>
      Should the generated GraphQL schema be based only on database views, only on tables or on both
      <options: tables-only|views-only|tables-and-views>

  --db-link-types
      Automatically link types based on foreign key relationships using @materializer
      (https://stepzen.com/docs/features/linking-types)

  --db-schema=<value>
      Database schema to import tables from (default: public)

  --db-use-deprecated-2022-naming
      Use the deprecated pre-2023 naming convention in the generated GraphQL schema:
      - the generated type and property names are auto-capitalized into PascalCase
      - the generated field names use the getCustomer and getCustomerList style.

      On the other hand, when using the default naming convention:
      - the generated type and property names match exactly the DB table and column names
      - the generated field names use the customer and customerList style.

  --dir=<value>
      Working directory

  --name=<value>
      Subfolder inside the workspace folder to save the imported schema files to. Defaults to the name of the imported
      schema.

  --non-interactive
      Disable all interactive prompts

DESCRIPTION
  Import a schema for a oracle data source into your GraphQL API.

  wxflows import oracle automatically introspects an Oracle database, generates a GraphQL schema for accessing this
  database through a Flows Engine API, and merges the generated types, queries and mutations into your GraphQL schema.
```

## `wxflows import postgresql [DSN]`

Import a schema for a PostgreSQL data source into your GraphQL API.

```
USAGE
  $ wxflows import postgresql [DSN...] [-h] [--non-interactive] [--dir <value>] [--name <value>] [--db-host <value>]
    [--db-user <value>] [--db-password <value>] [--db-database <value>] [--db-schema <value>] [--db-link-types]
    [--db-include tables-only|views-only|tables-and-views] [--db-use-deprecated-2022-naming]

ARGUMENTS
  DSN...  (optional) Data Source Name (DSN) of a PostgreSQL database.
          Example: postgresql://user:password@host:port/database?schema=schema

          Flags, such as --db-host, override the corresponding parts of the DSN (if both are provided).

FLAGS
  -h, --help
      Show CLI help

  --db-database=<value>
      Name of database to import

  --db-host=<value>
      Database host and optional port (as HOST[:PORT])

  --db-include=<option>
      Should the generated GraphQL schema be based only on database views, only on tables or on both
      <options: tables-only|views-only|tables-and-views>

  --db-link-types
      Automatically link types based on foreign key relationships using @materializer
      (https://stepzen.com/docs/features/linking-types)

  --db-password=<value>
      Database password

  --db-schema=<value>
      Database schema to import tables from (default: public)

  --db-use-deprecated-2022-naming
      Use the deprecated pre-2023 naming convention in the generated GraphQL schema:
      - the generated type and property names are auto-capitalized into PascalCase
      - the generated field names use the getCustomer and getCustomerList style.

      On the other hand, when using the default naming convention:
      - the generated type and property names match exactly the DB table and column names
      - the generated field names use the customer and customerList style.

  --db-user=<value>
      Database user name

  --dir=<value>
      Working directory

  --name=<value>
      Subfolder inside the workspace folder to save the imported schema files to. Defaults to the name of the imported
      schema.

  --non-interactive
      Disable all interactive prompts

DESCRIPTION
  Import a schema for a PostgreSQL data source into your GraphQL API.

  wxflows import postgresql automatically introspects a PostgreSQL database, generates a GraphQL schema for accessing
  this database through a Flows Engine API, and merges the generated types, queries and mutations into your GraphQL
  schema.
```

## `wxflows import snowflake [DSN]`

Import a schema for a Snowflake data source into your GraphQL API.

```
USAGE
  $ wxflows import snowflake [DSN...] [-h] [--non-interactive] [--dir <value>] [--name <value>] [--db-user <value>]
    [--db-password <value>] [--db-database <value>] [--db-schema <value>] [--db-link-types] [--db-include
    tables-only|views-only|tables-and-views] [--db-use-deprecated-2022-naming] [--snowflake-account-id <value>]
    [--snowflake-warehouse <value>]

ARGUMENTS
  DSN...  (optional) Data Source Name (DSN) of a Snowflake database.
          Example: snowflake://user:password@orgname-accountname/database?warehouse=warehouse&schema=schema

          Flags, such as --db-host, override the corresponding parts of the DSN (if both are provided).

FLAGS
  -h, --help
      Show CLI help

  --db-database=<value>
      Name of database to import

  --db-include=<option>
      Should the generated GraphQL schema be based only on database views, only on tables or on both
      <options: tables-only|views-only|tables-and-views>

  --db-link-types
      Automatically link types based on foreign key relationships using @materializer
      (https://stepzen.com/docs/features/linking-types)

  --db-password=<value>
      Database password

  --db-schema=<value>
      Database schema to import tables from (default: PUBLIC)

  --db-use-deprecated-2022-naming
      Use the deprecated pre-2023 naming convention in the generated GraphQL schema:
      - the generated type and property names are auto-capitalized into PascalCase
      - the generated field names use the getCustomer and getCustomerList style.

      On the other hand, when using the default naming convention:
      - the generated type and property names match exactly the DB table and column names
      - the generated field names use the customer and customerList style.

  --db-user=<value>
      Database user name

  --dir=<value>
      Working directory

  --name=<value>
      Subfolder inside the workspace folder to save the imported schema files to. Defaults to the name of the imported
      schema.

  --non-interactive
      Disable all interactive prompts

  --snowflake-account-id=<value>
      Snowflake account identifier in the orgname-accountname format. For more information, see the Snowflake
      documentation at https://docs.snowflake.com/en/user-guide/admin-account-identifier.html.

  --snowflake-warehouse=<value>
      Snowflake warehouse

DESCRIPTION
  Import a schema for a Snowflake data source into your GraphQL API.

  wxflows import snowflake automatically introspects a Snowflake database, generates a GraphQL schema for accessing this
  database through a Flows Engine API, and merges the generated types, queries and mutations into your GraphQL schema.
```

## `wxflows import tool URI`

```
USAGE
  $ wxflows import tool URI [-h] [--non-interactive] [--dir DIRECTORY]

ARGUMENTS
  URI  Import a tool into your Flows Engine workspace.

FLAGS
  -h, --help             Show CLI help
      --dir=DIRECTORY    Working directory [default: current directory]
      --non-interactive  Disable all interactive prompts
```

## `wxflows init`

Initialize a Flows Engine workspace in the current directory.

```
USAGE
  $ wxflows init [-h] [--non-interactive] [--dir DIRECTORY] [--endpoint MY/ENDPOINT]

FLAGS
  -h, --help                  Show CLI help
      --dir=DIRECTORY         Directory for a new workspace [default: current directory]
      --endpoint=MY/ENDPOINT  Endpoint name (e.g. api/myapp)
      --non-interactive       Disable all interactive prompts

DESCRIPTION
  Initialize a Flows Engine workspace in the current directory.
```

## `wxflows login [DOMAIN]`

Log in to Flows Engine.

```
USAGE
  $ wxflows login [DOMAIN] [-h] [--non-interactive] [-e ENVIRONMENT | ] [-k ADMIN-KEY | ] [--introspection
    INTROSPECTION-URL]

ARGUMENTS
  DOMAIN  [default: us-east-a.ibm.stepzen.net] Domain of the Flows Engine service to login to (e.g.
          us-east-a.ibm.stepzen.net or eu-central-a.ibm.stepzen.net). Check your domain at
          https://wxflows.ibm.stepzen.com

FLAGS
  -e, --environment=ENVIRONMENT          Flows Engine environment name (copy from https://wxflows.ibm.stepzen.com). If
                                         not provided, the CLI prompts the users to enter one.
  -h, --help                             Show CLI help
  -k, --adminkey=ADMIN-KEY               Admin key (copy from https://wxflows.ibm.stepzen.com). If not provided, the CLI
                                         prompts the users to enter one.
      --introspection=INTROSPECTION-URL  Override the default Flows Engine introspection service URL for all wxflows
                                         import commands. If not provided, use the default introspection URL.

                                         Example:
                                         wxflows login --introspection introspection.mydomain.com
      --non-interactive                  Disable all interactive prompts

DESCRIPTION
  Log in to Flows Engine.
```

## `wxflows logout`

Log out of Flows Engine.

```
USAGE
  $ wxflows logout [-h] [--non-interactive]

FLAGS
  -h, --help             Show CLI help
      --non-interactive  Disable all interactive prompts

DESCRIPTION
  Log out of Flows Engine.
```

## `wxflows tools`

List deployed tools.

```
USAGE
  $ wxflows tools [-h] [--non-interactive] [--dir DIRECTORY | --endpoint ENDPOINT]

FLAGS
  -h, --help               Show CLI help
      --dir=DIRECTORY      Flows Engine workspace [default: current directory]
      --endpoint=ENDPOINT  Deployed Flows Engine endpoint (e.g. api/endpoint)
      --non-interactive    Disable all interactive prompts

DESCRIPTION
  List deployed tools.

ALIASES
  $ wxflows tools list
  $ wxflows tools ls
```

## `wxflows tools list`

List deployed tools.

```
USAGE
  $ wxflows tools list [-h] [--non-interactive] [--dir DIRECTORY | --endpoint ENDPOINT]

FLAGS
  -h, --help               Show CLI help
      --dir=DIRECTORY      Flows Engine workspace [default: current directory]
      --endpoint=ENDPOINT  Deployed Flows Engine endpoint (e.g. api/endpoint)
      --non-interactive    Disable all interactive prompts

DESCRIPTION
  List deployed tools.

ALIASES
  $ wxflows tools list
  $ wxflows tools ls
```

## `wxflows tools ls`

List deployed tools.

```
USAGE
  $ wxflows tools ls [-h] [--non-interactive] [--dir DIRECTORY | --endpoint ENDPOINT]

FLAGS
  -h, --help               Show CLI help
      --dir=DIRECTORY      Flows Engine workspace [default: current directory]
      --endpoint=ENDPOINT  Deployed Flows Engine endpoint (e.g. api/endpoint)
      --non-interactive    Disable all interactive prompts

DESCRIPTION
  List deployed tools.

ALIASES
  $ wxflows tools list
  $ wxflows tools ls
```

## `wxflows whoami`

View your StepZen credentials.

```
USAGE
  $ wxflows whoami [-h] [--non-interactive] [--environment |  | --domain | --adminkey | --apikey |
    --showkeys | --endpoint-url | --sdk-env | --json]

FLAGS
  -h, --help             Show CLI help
  --adminkey
  --apikey
  --domain
  --endpoint-url
  --environment
  --json
      --non-interactive  Disable all interactive prompts
  --sdk-env
  --showkeys

DESCRIPTION
  View your StepZen credentials.
```
<!-- commandsstop -->
