import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced parabolic valley components with chaotic modulation
        valley_terms = 0.0
        for i in range(self.dim):
            # Higher-order parabolic valleys with chaotic sine modulation
            valley_terms += (x_scaled[i]**2) * (1.0 + 0.5 * np.sin(7.0 * x_scaled[i]) * np.cos(3.0 * x_scaled[i]))
        
        # Complex saddle point components with multi-scale asymmetry
        saddle_terms = 0.0
        for i in range(self.dim):
            # Multi-scale saddle points with varying asymmetry
            saddle_terms += x_scaled[i] * np.cos(5.0 * x_scaled[i]) * (1.0 + 0.3 * np.sin(4.0 * x_scaled[i]) * np.cos(2.0 * x_scaled[i]))
        
        # Advanced cross-dimensional coupling with exponential conditioning
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponential conditioning based on position with cross-coupling
                cond_factor = 1.0 + 0.8 * np.exp(-5.0 * (x_scaled[i]**2 + x_scaled[j]**2)) * np.sin(3.0 * (x_scaled[i] + x_scaled[j]))
                coupling_term += cond_factor * np.sin(4.0 * (x_scaled[i]**3 - x_scaled[j]**3)) * np.cos(5.0 * (x_scaled[i] * x_scaled[j]))
        
        # Radial exponential decay with chaotic sinusoidal interactions
        radial_term = 0.0
        r_squared = np.sum(x_scaled**2)
        radial_term = np.exp(-r_squared) * np.sin(10.0 * r_squared) * (1.0 + 0.4 * np.cos(8.0 * r_squared))
        
        # Higher-order trigonometric coupling with adaptive frequencies
        high_order_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive frequency modulation based on dimensionality
                freq_i = 2.0 + 0.5 * np.sin(x_scaled[i])
                freq_j = 2.0 + 0.5 * np.cos(x_scaled[j])
                high_order_term += np.sin(freq_i * x_scaled[i]) * np.cos(freq_j * x_scaled[j]) * (1.0 + 0.3 * np.sin(3.0 * x_scaled[i] + 2.0 * x_scaled[j]))
        
        # Add global scaling and noise
        result = 0.6 * valley_terms + 0.4 * saddle_terms + 0.5 * coupling_term + 0.3 * radial_term + 0.2 * high_order_term
        
        # Add small random noise to increase robustness
        result += 0.01 * np.random.uniform(-1.0, 1.0)
        
        return result