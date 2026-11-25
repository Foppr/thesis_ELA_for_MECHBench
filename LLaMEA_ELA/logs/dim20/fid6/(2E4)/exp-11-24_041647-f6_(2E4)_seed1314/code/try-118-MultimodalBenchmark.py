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
            # Slightly modified coefficients for enhanced complexity
            a = 1.2 + 0.2 * np.sin(i * 0.6)
            b = 0.8 + 0.3 * np.cos(i * 0.4)
            c = 0.5 + 0.15 * np.sin(i * 0.8)
            
            # Enhanced chaotic modulation with higher frequency components
            saddle_term += a * x_normalized[i]**2 + b * x_normalized[i]**4 + c * np.sin(7 * x_normalized[i])
        
        # Embedded periodic potentials with altered frequencies and amplitudes
        periodic_term = 0.0
        for i in range(self.dim):
            # Modified frequency and amplitude parameters
            freq = 3**(i % 4) * (1 + 0.15 * np.sin(i * 0.5))
            amp = 2.0 + 0.4 * np.cos(i * 0.7)
            periodic_term += amp * np.cos(freq * x_normalized[i]) * np.exp(-0.3 * x_normalized[i]**2)
        
        # Dynamic coupling between dimensions with modified interaction strengths
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Altered coupling coefficient with different modulation
                coupling_strength = 0.6 * (1 + np.sin(0.4 * i + 0.3 * j))
                coupling_term += coupling_strength * x_normalized[i] * x_normalized[j] * np.exp(-0.15 * (x_normalized[i] - x_normalized[j])**2)
        
        # Asymmetric gradient flow with modified multi-scale chaotic modulation
        flow_term = 0.0
        for i in range(self.dim):
            # Modified modulator with additional nonlinear component
            modulator = 1.0 + 0.4 * np.sin(8 * x_normalized[i] + 2.5 * np.cos(3 * x_normalized[i]))
            flow_term += modulator * np.tanh(x_normalized[i]) * (1 + 0.25 * np.sin(i * 0.6))
        
        # Fractional-order curvature with modified scaling and memory effects
        curvature_term = 0.0
        for i in range(self.dim):
            # Slightly different fractional order for increased difficulty
            order = 1.4 + 0.25 * np.sin(i * 0.3)
            curvature_term += np.abs(x_normalized[i])**order
        
        # Combined function with adjusted weights for enhanced multimodality
        return (0.28 * saddle_term + 
                0.27 * periodic_term + 
                0.22 * coupling_term + 
                0.16 * flow_term + 
                0.07 * curvature_term)