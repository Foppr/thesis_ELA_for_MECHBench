import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperbolic tangent basin terms with varying steepness and chaotic modulation
        basin_term = 0.0
        for i in range(self.dim):
            steepness = 1.5 + 0.8 * np.sin(i * 0.9 + np.cos(i * 0.3))
            basin_term += (np.tanh(steepness * x[i])**3) * np.exp(-0.15 * x[i]**2) * (1.0 + 0.2 * np.sin(3.0 * x[i]))
        
        # Polynomial gradient flow components with mixed exponents and frequency modulation
        grad_term = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.3 * np.cos(i * 0.5)
            grad_term += (0.4 * x[i]**2 + 0.2 * x[i]**4 + 0.05 * np.exp(0.6 * x[i])) * np.cos(freq_mod * x[i]) * np.sin(0.4 * x[i])
        
        # Logarithmic energy interactions with chaotic coupling coefficients
        energy_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                coupling = 1.0 + 0.1 * np.sin(x[i] + x[j]) * np.cos(2.0 * x[i])
                energy_term += (np.log(dist + 1.5) / (dist + 0.5)) * coupling * np.sin(2.5 * x[i]) * np.cos(1.8 * x[j])
        
        # Chaotic saddle-point modulation with higher-order sinusoidal perturbations
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += (np.sin(x[i]) * np.cos(x[i]) * 
                           np.exp(-0.12 * np.abs(x[i])) * 
                           np.sin(3.5 * x[i] + np.sin(2.5 * x[i]) + 0.5 * np.sin(4.0 * x[i])))
        
        # Global scaling with fractal-like polynomial and exponential components
        global_term = 0.0
        for i in range(self.dim):
            global_term += (0.5 * x[i]**3 * np.exp(-0.12 * x[i]**2) + 
                          0.25 * x[i] * np.sin(0.6 * x[i]) + 
                          0.15 * np.log(np.abs(x[i]) + 2.5) + 
                          0.05 * np.sin(5.0 * x[i]))
        
        # Add multi-scale harmonic coupling terms
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += (0.3 * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i]) + 
                            0.2 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[i]) + 
                            0.1 * np.sin(6.0 * x[i]))
        
        # Return the combined function value with enhanced regularization
        return basin_term + grad_term + energy_term + chaotic_term + global_term + harmonic_term + 0.01 * np.sum(x**2)