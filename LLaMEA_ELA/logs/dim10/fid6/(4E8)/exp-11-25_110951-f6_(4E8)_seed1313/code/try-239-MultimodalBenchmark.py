import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Perturbed exponential decay potentials with chaotic modulation and multi-scale interference
        potential_term = 0.0
        for i in range(self.dim):
            potential_term += np.exp(-np.abs(x_norm[i]) * 0.8) * (1 + 0.7 * np.sin(3.5 * x_norm[i]) + 
                                                           0.5 * np.sin(7.5 * x_norm[i]) * np.cos(11.5 * x_norm[i]) +
                                                           0.25 * np.sin(15.5 * x_norm[i])**2)
        
        # Multi-frequency sinusoidal modulations with fractal-like structure and asymmetric coupling
        sinusoidal_term = 0.0
        frequencies = [2.5, 4.5, 6.5, 8.5, 10.5, 12.5]
        for i in range(self.dim):
            for j, freq in enumerate(frequencies):
                sinusoidal_term += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] / (j + 1.5)) * \
                                  np.sin(2 * np.pi * x_norm[i] * (j + 1.5)) * \
                                  np.exp(-0.12 * (x_norm[i] - x_norm[(i+1)%self.dim])**2)
        
        # Asymmetric elliptic structures with cross-dimensional coupling, chaotic interference, and polynomial scaling
        elliptic_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            l = (i + 3) % self.dim
            elliptic_term += (x_norm[i]**2 + 0.6 * x_norm[j]**2 + 0.4 * x_norm[k]**2 + 
                             0.2 * x_norm[l]**2) * \
                           np.sin(2 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[j]) * \
                           np.exp(-0.15 * (x_norm[i] - x_norm[j])**2) * \
                           (1 + 0.4 * np.sin(5.5 * x_norm[i]))
        
        # Multi-scale harmonic interference with amplitude modulation, chaotic coupling, and asymmetric scaling
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += (np.sin(10.5 * x_norm[i]) * np.exp(-0.55 * x_norm[i]**2) + 
                             0.35 * np.cos(15.5 * x_norm[i]) * np.exp(-0.35 * x_norm[i]**2) +
                             0.12 * np.sin(25.5 * x_norm[i]) * np.cos(30.5 * x_norm[i]) +
                             0.06 * np.sin(40.5 * x_norm[i])**3)
        
        # Cross-dimensional interaction with polynomial coupling, fractal basin modification, and chaotic perturbation
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_term += ((x_norm[i] * x_norm[j])**3.5 + (x_norm[i] + x_norm[j])**2.5 + 
                            0.6 * np.sin(5.5 * x_norm[i]) * np.cos(5.5 * x_norm[j]) +
                            0.25 * np.sin(10.5 * x_norm[i]) * np.sin(10.5 * x_norm[j]))
        
        # Asymmetric gradient modulation with logarithmic scaling, chaotic perturbation, and multi-scale interference
        grad_term = 0.0
        for i in range(self.dim):
            grad_term += (np.log(1 + 1.2 * np.abs(x_norm[i])) * np.sin(5.5 * x_norm[i]) + 
                         0.25 * np.cos(13.5 * x_norm[i]) * np.sin(17.5 * x_norm[i]) +
                         0.15 * np.sin(20.5 * x_norm[i]) * np.cos(25.5 * x_norm[i]))
        
        # Fractal basin enhancement with multi-scale harmonic interference and chaotic scaling
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += (np.sin(50.5 * x_norm[i]) * np.cos(40.5 * x_norm[i]) + 
                            0.75 * np.sin(30.5 * x_norm[i])**2 * np.cos(20.5 * x_norm[i]) +
                            0.35 * np.cos(60.5 * x_norm[i]) * np.sin(70.5 * x_norm[i]))
        
        # Additional chaotic coupling terms for increased complexity
        chaos_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            chaos_term += np.sin(3.5 * x_norm[i]) * np.cos(7.5 * x_norm[j]) * \
                         np.sin(5.5 * x_norm[k]) * np.exp(-0.25 * (x_norm[i] - x_norm[j])**2)
        
        # Final combined function with dynamic weighting, chaotic scaling, and increased complexity
        return (0.22 * potential_term + 0.19 * sinusoidal_term + 0.17 * elliptic_term + 
                0.13 * harmonic_term + 0.10 * poly_term + 0.09 * grad_term + 0.11 * fractal_term +
                0.08 * chaos_term)