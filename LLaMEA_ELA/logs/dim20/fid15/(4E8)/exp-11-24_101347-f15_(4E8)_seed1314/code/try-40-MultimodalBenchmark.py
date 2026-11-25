import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Parabolic valley components with periodic modulation
        valley_terms = 0.0
        for i in range(self.dim):
            # Asymmetric parabolic valleys
            valley_terms += (x_scaled[i]**2) * (1.0 + 0.3 * np.sin(4.0 * x_scaled[i]))
        
        # Saddle point components with asymmetric structure
        saddle_terms = 0.0
        for i in range(self.dim):
            # Create asymmetric saddle points
            saddle_terms += x_scaled[i] * np.cos(3.0 * x_scaled[i]) * (1.0 + 0.2 * np.sin(2.0 * x_scaled[i]))
        
        # Cross-dimensional coupling with dynamic conditioning
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic conditioning based on position
                cond_factor = 1.0 + 0.5 * np.sin(2.0 * (x_scaled[i] + x_scaled[j]))
                coupling_term += cond_factor * np.sin(3.0 * (x_scaled[i]**2 - x_scaled[j]**2)) * np.cos(2.0 * (x_scaled[i] * x_scaled[j]))
        
        # Periodic modulation with multiple frequencies
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(5.0 * x_scaled[i]) * np.cos(7.0 * x_scaled[i]) * (1.0 + 0.1 * np.sin(3.0 * x_scaled[i]))
        
        # Add global scaling and noise
        result = 0.5 * valley_terms + 0.3 * saddle_terms + 0.4 * coupling_term + 0.2 * periodic_term
        
        # Add small random noise to increase robustness
        result += 0.01 * np.random.uniform(-1.0, 1.0)
        
        return result