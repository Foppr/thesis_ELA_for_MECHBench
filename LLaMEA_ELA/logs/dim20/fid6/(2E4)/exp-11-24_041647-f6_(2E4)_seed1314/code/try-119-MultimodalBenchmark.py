import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced chaotic saddle-point term with modified potential wells
        saddle_term = 0.0
        for i in range(self.dim):
            # Modified asymmetric quadratic potential with enhanced nonlinearity
            a = 1.2 + 0.4 * np.sin(i * 0.6)
            b = 0.8 + 0.3 * np.cos(i * 0.4)
            c = 0.5 + 0.2 * np.sin(i * 0.8)
            
            # Enhanced saddle point configuration with stronger chaotic modulation
            saddle_term += a * x_normalized[i]**2 + b * x_normalized[i]**4 + c * np.sin(7 * x_normalized[i])
        
        # Improved periodic potentials with frequency modulation and enhanced interference
        periodic_term = 0.0
        for i in range(self.dim):
            freq = 3**(i % 4) * (1 + 0.3 * np.sin(i * 0.5))
            amp = 2.0 + 0.6 * np.cos(i * 0.7)
            periodic_term += amp * np.cos(freq * x_normalized[i]) * np.exp(-0.3 * x_normalized[i]**2)
        
        # Refined dynamic coupling between dimensions with enhanced interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced coupling coefficient with stronger modulation
                coupling_strength = 0.7 * (1 + np.sin(0.4 * i + 0.3 * j))
                coupling_term += coupling_strength * x_normalized[i] * x_normalized[j] * np.exp(-0.2 * (x_normalized[i] - x_normalized[j])**2)
        
        # Improved asymmetric gradient flow with multi-scale chaotic modulation
        flow_term = 0.0
        for i in range(self.dim):
            # Enhanced multi-scale chaotic modulation of gradient direction
            modulator = 1.2 + 0.4 * np.sin(9 * x_normalized[i] + 3 * np.cos(4 * x_normalized[i]))
            flow_term += modulator * np.tanh(x_normalized[i]) * (1 + 0.3 * np.sin(i * 0.6))
        
        # Enhanced fractional-order curvature with memory effects and dynamic scaling
        curvature_term = 0.0
        for i in range(self.dim):
            order = 1.7 + 0.4 * np.sin(i * 0.5)
            curvature_term += np.abs(x_normalized[i])**order
        
        # Combined function with adjusted weights for better benchmark performance
        return (0.35 * saddle_term + 
                0.28 * periodic_term + 
                0.22 * coupling_term + 
                0.13 * flow_term + 
                0.02 * curvature_term)