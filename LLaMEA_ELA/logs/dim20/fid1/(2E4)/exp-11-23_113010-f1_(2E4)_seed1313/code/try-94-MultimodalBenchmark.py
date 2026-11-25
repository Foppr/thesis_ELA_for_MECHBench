import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponentially increasing polynomial basin with fractal-like complexity
        poly_basin = np.sum(np.exp(2 * np.abs(x_norm)) * (x_norm**6 + 0.8 * x_norm**5 + 0.6 * x_norm**4 + 0.4 * x_norm**3))
        
        # Sinusoidal modulations with exponentially increasing frequencies and prime-based coupling
        sin_mod = np.sum(np.sin(2**(np.arange(self.dim) + 1) * np.pi * x_norm) * 
                         np.cos(3**(np.arange(self.dim) + 1) * np.pi * x_norm))
        
        # Dynamic cross-dimensional coupling with prime-based interaction coefficients and exponential scaling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                prime_coeff = (i + 1) * (j + 1)  # Prime-inspired coupling
                cross_interaction += np.exp(prime_coeff * np.abs(x_norm[i] - x_norm[j])) * \
                                   np.sin(prime_coeff * np.pi * (x_norm[i] + x_norm[j]))
        
        # Saddle structure with chaotic exponential terms and asymmetric components
        saddle = np.sum(np.exp(3 * np.abs(x_norm)) * np.cos(5 * np.pi * x_norm) + 
                       0.7 * np.exp(2 * np.abs(x_norm)) * np.sin(4 * np.pi * x_norm) + 
                       0.5 * np.exp(np.abs(x_norm)) * np.cos(3 * np.pi * x_norm))
        
        # Multi-scale harmonic components with fractal-like frequency progression
        harmonic = np.sum(np.sin(10**(np.arange(self.dim) + 1) * np.pi * x_norm**2) * 
                          np.cos(11**(np.arange(self.dim) + 1) * np.pi * x_norm**2))
        
        # Chaotic noise with dynamic amplitude and exponentially modulated frequency
        noise = 0.05 * np.random.random() * np.sin(200 * np.pi * np.sum(np.exp(3 * np.abs(x_norm))))
        
        # Dynamic scaling factor based on dimensionality with exponential growth
        scale_factor = 1.0 + 0.1 * np.log(self.dim) + 0.02 * np.exp(0.1 * self.dim)
        
        return scale_factor * (1.5 * poly_basin + 1.3 * sin_mod + 0.8 * cross_interaction + 
                              0.6 * saddle + 0.4 * harmonic + noise)