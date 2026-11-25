import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic gradient component with nested sinusoids
        chaotic_grad = 0.0
        for i in range(self.dim):
            chaotic_grad += np.sin(12.0 * x_scaled[i]) * np.cos(8.0 * x_scaled[i]) * np.sin(4.0 * x_scaled[i])
        
        # Nested multi-scale sinusoidal modulations
        nested_mod = 0.0
        for i in range(self.dim):
            nested_mod += (1.0 + 0.6 * np.sin(25.0 * x_scaled[i])) * \
                         (1.0 + 0.4 * np.cos(20.0 * x_scaled[i])) * \
                         (1.0 + 0.5 * np.sin(10.0 * x_scaled[i]))
        
        # Dynamic scaling factor based on distance from center
        r = np.sqrt(np.sum(x_scaled**2))
        dynamic_scale = 1.0 + 0.9 * np.exp(-r**2 / 1.5) + 0.4 * np.sin(6.0 * r)
        
        # Adaptive penalty with multiple constraint violations
        penalty = 0.0
        for i in range(self.dim):
            if abs(x_scaled[i]) > 0.75:
                penalty += 12.0 * (abs(x_scaled[i]) - 0.75)**2
            if x_scaled[i] * x_scaled[(i+1) % self.dim] < -0.4:
                penalty += 6.0 * (x_scaled[i] * x_scaled[(i+1) % self.dim] + 0.4)**2
        
        # Multi-modal structure with varying amplitude and frequency
        modal_structure = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.8 * np.sin(15.0 * x_scaled[i])
            freq = 6.0 + 4.0 * np.cos(10.0 * x_scaled[i])
            modal_structure += amp * np.sin(freq * x_scaled[i] + 2.5 * np.cos(5.0 * x_scaled[i]))
        
        # Cross-dimensional coupling with dynamic weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_scaled[i] - x_scaled[j])
                weight = 0.6 + 0.4 * np.sin(3.0 * dist)
                cross_coupling += weight * np.sin(18.0 * dist) * np.cos(12.0 * dist)
        
        # Combine all components with dynamic weighting
        result = (dynamic_scale * 
                 (0.5 * chaotic_grad + 0.4 * nested_mod + 0.5 * modal_structure + 0.3 * cross_coupling) + 
                 0.15 * penalty)
        
        return result