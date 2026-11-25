import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced polynomial basin with chaotic coefficient modulation and higher-order terms
        poly_basin = np.sum(0.6 * x_norm**9 + 0.3 * x_norm**8 + 0.4 * x_norm**7 + 0.1 * x_norm**6 + 0.2 * x_norm**5)
        
        # Sinusoidal modulations with chaotic frequency ratios, prime-based harmonics, and fractal-like complexity
        sin_mod = np.sum(np.sin(9 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) * np.sin(13 * np.pi * x_norm))
        sin_mod2 = np.sum(np.sin(21 * np.pi * x_norm**2) * np.cos(17 * np.pi * x_norm**2) * np.sin(19 * np.pi * x_norm**2))
        
        # Enhanced cross-dimensional coupling with chaotic quartic interaction terms and prime-based coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += (x_norm[i]**4 + x_norm[j]**4) * np.sin(5 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Perturbed saddle structure with chaotic higher-order terms, asymmetric components, and dynamic scaling
        saddle = np.sum(x_norm**8 * np.cos(8 * np.pi * x_norm) + 0.6 * x_norm**7 * np.sin(7 * np.pi * x_norm) + 0.4 * x_norm**6 * np.cos(6 * np.pi * x_norm))
        
        # Additional harmonic components with fractal-like complexity and chaotic phase shifts
        harmonic = np.sum(np.sin(25 * np.pi * x_norm**3) * np.cos(21 * np.pi * x_norm**3) * np.sin(27 * np.pi * x_norm**3))
        
        # Chaotic noise with dynamic amplitude and frequency modulation
        noise = 0.03 * np.random.random() * np.sin(120 * np.pi * np.sum(x_norm**2))
        
        # Dynamic scaling factor based on dimensionality
        scale_factor = 1.0 + 0.15 * np.log(self.dim)
        
        return scale_factor * (1.8 * poly_basin + 1.2 * sin_mod + 0.9 * sin_mod2 + 0.7 * cross_interaction + 0.5 * saddle + 0.6 * harmonic + noise)