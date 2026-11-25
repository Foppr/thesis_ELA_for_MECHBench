import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Chaotic saddle-point term with dynamic coupling and asymmetric potential wells
        saddle_term = 0.0
        for i in range(self.dim):
            # Asymmetric quadratic potential with dynamic coefficients
            a = 1.0 + 0.3 * np.sin(i * 0.5)
            b = 0.7 + 0.2 * np.cos(i * 0.3)
            c = 0.4 + 0.1 * np.sin(i * 0.7)
            
            # Saddle point configuration with chaotic modulation
            saddle_term += a * x_normalized[i]**2 + b * x_normalized[i]**4 + c * np.sin(5 * x_normalized[i])
        
        # Embedded periodic potentials with dynamic frequencies and amplitudes
        periodic_term = 0.0
        for i in range(self.dim):
            freq = 2**(i % 3) * (1 + 0.2 * np.sin(i * 0.4))
            amp = 1.5 + 0.5 * np.cos(i * 0.6)
            periodic_term += amp * np.cos(freq * x_normalized[i]) * np.exp(-0.5 * x_normalized[i]**2)
        
        # Dynamic coupling between dimensions with time-varying interaction strengths
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Time-varying coupling coefficient
                coupling_strength = 0.5 * (1 + np.sin(0.3 * i + 0.2 * j))
                coupling_term += coupling_strength * x_normalized[i] * x_normalized[j] * np.exp(-0.1 * (x_normalized[i] - x_normalized[j])**2)
        
        # Asymmetric gradient flow with multi-scale chaotic modulation
        flow_term = 0.0
        for i in range(self.dim):
            # Multi-scale chaotic modulation of gradient direction
            modulator = 1.0 + 0.3 * np.sin(7 * x_normalized[i] + 2 * np.cos(3 * x_normalized[i]))
            flow_term += modulator * np.tanh(x_normalized[i]) * (1 + 0.2 * np.sin(i * 0.5))
        
        # Fractional-order curvature with memory effects and dynamic scaling
        curvature_term = 0.0
        for i in range(self.dim):
            order = 1.5 + 0.3 * np.sin(i * 0.4)
            curvature_term += np.abs(x_normalized[i])**order
        
        # Combined function with weighted contributions from different landscape features
        return (0.3 * saddle_term + 
                0.25 * periodic_term + 
                0.2 * coupling_term + 
                0.15 * flow_term + 
                0.1 * curvature_term)