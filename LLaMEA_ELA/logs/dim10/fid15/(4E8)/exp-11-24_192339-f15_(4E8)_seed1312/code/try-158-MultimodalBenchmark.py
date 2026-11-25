import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal oscillation with chaotic modulation
        sin_component = 0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(0.4 * x[i]) * np.cos(0.2 * x[i])
            sin_component += np.sin(freq * x[i]) * np.tanh(x[i] / 2.0) * np.exp(-0.1 * x[i]**2)
        
        # Dynamic radial basis function with quaternion-inspired interactions
        rbf = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                width = 1.0 + 0.5 * np.sin(0.3 * (x[i] + x[j]))
                rbf += np.exp(-0.5 * (dist / width)**2) * np.cos(3 * np.pi * dist) * np.tanh(dist)
        
        # Enhanced polynomial coupling with hyperbolic tangent interactions
        poly_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                term = (x[i]**3 + x[j]**3) * np.tanh(0.5 * (x[i] - x[j]))
                poly_coupling += term * (1.0 + 0.4 * np.abs(x[i] - x[j]) * np.cosh(x[i] + x[j]))
        
        # Cross-dimensional hyperbolic tangent interactions with dynamic conditioning
        cond = 0
        for i in range(self.dim):
            cond += np.tanh(0.5 * x[i]) * np.exp(0.2 * np.abs(x[i])) * (1.0 + 0.3 * np.sin(0.7 * x[i]))
        
        # Novel hyperbolic tangent-based noise with fractal-like characteristics
        noise = 0.1 * np.sum(np.tanh(5 * x) ** 2 + 0.2 * np.cosh(3 * x) ** 2 - 1)
        
        # Quaternion-inspired global shift and scaling factor
        shift = 0.3 * np.sum(x**4 * np.sin(0.5 * x))
        scale_factor = 1.5 + 0.5 * np.tanh(np.sum(x**2) / self.dim)
        
        # Intensified chaotic modulation with additional fractal components
        chaotic_mod = 0
        for i in range(self.dim):
            chaotic_mod += np.sin(10 * np.sin(x[i])) * np.cos(7 * x[i]) * np.tanh(x[i]**3)
        
        # Additional high-frequency oscillation component
        high_freq = 0
        for i in range(self.dim):
            high_freq += np.sin(20 * x[i]) * np.cos(15 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Combine all components with optimized weights and chaotic modulation
        return scale_factor * (0.6 * sin_component + 0.25 * rbf + 0.35 * poly_coupling + 
                              0.15 * cond + 0.1 * chaotic_mod + 0.05 * high_freq) + shift + noise