U
    }��^�  �                   @   s�   d dl Z d dlZd dlZd dlmZ dd� ZdZdZdZdZ	d	Z
d
ZdZdZdZdZdZdZd
ZdZdZdZdZdZdZdZdd� Zdd� Zdd� Ze�  dS )�    N)�logoc                 C   s2   | d D ]$}t j�|� t j��  t�d� qd S )N�
gl�l��?)�sys�stdout�write�flush�time�sleep)�s�x� r   �/sdcard/BASHENC.py�ketik   s    
r   z[32;1mz[0;32mz[34;1mz[36;1mz[31;1mz[0mz[37;1mz[35;1mz[3;1mz[33;1mz[0;33mz[30;1mz[31mz[1;32mz[33mz[34mz[35mz[36mz[37mc                   C   s"   t �d� t �d� t �d� d S )Nz)pkg install update && pkg install upgradezpkg install nodejsznpm install -g bash-obfuscate)�os�systemr   r   r   r   �install   s    

r   c               
   C   s�   t �d� t��  ttt� dt� dt� dt� d���} ttt� dt� dt� dt� d���}t �d|  d | � t	|d	��
d
�}tt� dt� dt� dt� d�| � d S )N�clear�[�*�] z
PATH FILE:zOUTPUT PATH:zbash-obfuscate z -o �az
#YOUTUBE BENJAMImN ID"zSCRIPT TERSIMPAN DI )r   r   r   �banner�str�input�mens�kuli�kt�openr   r   r   �k)ZgaZabinZabir   r   r   �mulai#   s    
$$r   c               	   C   s�   t ��  tt� dt� dt� dt� d�� tt� dt� dt� dt� d�� tt� dt� dt� d	��} | dkrxt�  t	�  n| dkr�t	�  d S )
Nr   �1r   zINSTALL BAHAN�2zLOGIN TOOLSu   •ZPILIH�:)
r   r   r   �aqur   �smpr   r   r   r   )�gr   r   r   �bahan,   s      r&   )r   r   r   Zabinkunsr   r   r%   �gtZbt�b�m�c�p�uZzesr   r   r   r#   r   Zmenr   Zsmar$   Zsd�zr   r   r&   r   r   r   r   �<module>   s4   	
