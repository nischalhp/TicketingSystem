PGDMP                           r            postgres    9.3.3    9.3.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            �            1259    50822    transactions    TABLE     �   CREATE TABLE transactions (
    vehicle_type integer,
    toll_type integer,
    "timestamp" timestamp without time zone,
    price double precision,
    id uuid DEFAULT uuid_generate_v4() NOT NULL,
    vehicle_no character varying(20)
);
     DROP TABLE public.transactions;
       public         postgres    false            �          0    50822    transactions 
   TABLE DATA               \   COPY transactions (vehicle_type, toll_type, "timestamp", price, id, vehicle_no) FROM stdin;
    public       postgres    false    171   �       U           2606    50827    transactions_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY transactions
    ADD CONSTRAINT transactions_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.transactions DROP CONSTRAINT transactions_pkey;
       public         postgres    false    171    171            W           2606    58985 %   transactions_vehicle_no_timestamp_key 
   CONSTRAINT     y   ALTER TABLE ONLY transactions
    ADD CONSTRAINT transactions_vehicle_no_timestamp_key UNIQUE (vehicle_no, "timestamp");
 \   ALTER TABLE ONLY public.transactions DROP CONSTRAINT transactions_vehicle_no_timestamp_key;
       public         postgres    false    171    171    171            �   �   x�u�+NDAFa�wl�'�ꮺ�p$x��!��~&��
�����pb9�_�n�J�Ez�=P�,v�XܱHu{�T���!?,"��Ee��8��H=a���X;��r�*���)�Rr��j�97�	�+�1�觹V[�Rz�����t��Ø:�&A��]}�Tz��^���kOD{     