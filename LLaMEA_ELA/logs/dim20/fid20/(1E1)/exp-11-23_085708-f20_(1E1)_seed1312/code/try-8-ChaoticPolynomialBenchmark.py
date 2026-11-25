import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute hyperchaotic sine-cosine map constants
        self.hyperchaos = np.array([0.5] * dim)
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Higher-order polynomial coupling terms - creates extremely complex interaction
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    poly_term += (x[i]**4) * (x[j]**3) * (x[k]**2) + (x[i]**2) * (x[j]**4) * (x[k]**3)
        
        # Hyperchaotic sine-cosine map interaction - introduces extreme sensitivity
        hyperchaos_interaction = 0.0
        for i in range(self.dim):
            # Apply hyperchaotic sine-cosine dynamics
            sin_val = np.sin(x[i])
            cos_val = np.cos(x[i])
            hyperchaos_val = sin_val * cos_val + 0.5 * np.sin(2 * x[i]) * np.cos(2 * x[i])
            hyperchaos_interaction += hyperchaos_val * (x[i]**1.5)
            
        # Dynamic fractal-like radial component with time-varying exponents
        fractal_term = 0.0
        for i in range(self.dim):
            r = np.abs(x[i])
            # Time-varying exponents to create dynamic fractal structure
            exponent = 2.0 + 1.5 * np.sin(i * 0.7) * np.cos(i * 0.3)
            fractal_term += r**exponent
            
        # Dynamic noise component with position-dependent amplitude and frequency
        dynamic_noise = 0.0
        for i in range(self.dim):
            # Noise amplitude varies with solution position and dimension
            noise_amplitude = 0.2 * (1 + np.abs(x[i]) / 5.0) * (1 + 0.5 * np.sin(i))
            noise_frequency = 10 + 5 * np.cos(i)
            dynamic_noise += noise_amplitude * np.sin(noise_frequency * x[i])
            
        # Cross-dimensional coupling with phase shifts
        cross_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            cross_coupling += np.sin(x[i] + 0.3 * x[j]) * np.cos(0.7 * x[i] - 0.5 * x[j])
            
        # Combined function value with additional global scaling
        return poly_term + hyperchaos_interaction + fractal_term + dynamic_noise + cross_coupling + 5.0