import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced polynomial base term with mixed powers and adaptive conditioning
        polynomial = np.sum(x_scaled**4) + 0.5 * np.sum(x_scaled**6) + 0.3 * np.sum(x_scaled**8)
        
        # Stronger trigonometric components with variable frequencies, amplitudes, and phase shifts
        trigonometric = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi * (1.5 + 0.3 * np.sin(i * 0.7))
            amplitude = 1.0 / (1.0 + 0.5 * i + 0.1 * np.cos(i * 0.3))
            phase_shift = 0.5 * np.sin(i * 0.4)
            trigonometric += amplitude * np.cos(freq * x_scaled[i] + phase_shift) * np.sin(freq * x_scaled[i] + phase_shift)
        
        # Exponential decay components with stronger cross-terms and additional coupling
        exponential = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_term = np.exp(-0.3 * (x_scaled[i]**2 + x_scaled[j]**2))
                cross_term = np.sin(5 * x_scaled[i] * x_scaled[j]) * np.cos(3 * x_scaled[i] * x_scaled[j])
                exponential += exp_term * cross_term
        
        # Non-separable interaction terms with cubic components, phase shifts, and dynamic weights
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 / (1.0 + 0.2 * np.abs(x_scaled[i] - x_scaled[j]))
                interaction += weight * (x_scaled[i]**3 + x_scaled[j]**3) * np.sin(5 * x_scaled[i] * x_scaled[j])
        
        # Additional quadratic and cubic terms with enhanced complexity
        quadratic = 0.8 * np.sum(x_scaled**2)
        cubic = 0.3 * np.sum(x_scaled**3)
        
        # Cross-dimensional coupling with sine and cosine interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.sin(2 * x_scaled[i]) * np.cos(2 * x_scaled[j]) * (x_scaled[i] + x_scaled[j])**2
        
        # Global scaling and combination
        return 6.0 * polynomial + 4.0 * trigonometric + 2.5 * exponential + 2.0 * interaction + 1.2 * quadratic + 0.5 * cubic + 0.8 * cross_coupling