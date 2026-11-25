import numpy as np

class ChaoticSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameter for sine mapping
        self.a = 3.8
        # Initialize chaotic sequence using sine map
        self.chaos_seq = self._initialize_chaos()
        
    def _initialize_chaos(self):
        # Generate chaotic sequence using sine map
        seq = np.zeros(self.dim)
        x = 0.5
        for i in range(self.dim):
            x = np.sin(self.a * x)
            seq[i] = x
        return seq
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial potential component
        poly_sum = 0
        for i in range(self.dim):
            poly_sum += (x[i]**4 + 0.3 * x[i]**3 + 1.5 * x[i]**2 + 0.2 * x[i])
            
        # Radial basis function component
        rbf_sum = 0
        for i in range(self.dim):
            # Use chaotic sequence for RBF centers and widths
            center = self.chaos_seq[i] * 3.0
            width = 0.5 + 0.5 * np.abs(self.chaos_seq[i])
            rbf_sum += np.exp(-0.5 * ((x[i] - center) / width)**2)
            
        # Trigonometric coupling terms with chaotic weights
        trig_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.4 + 0.6 * np.cos(self.chaos_seq[i] * self.chaos_seq[j])
                trig_sum += weight * np.sin(x[i]) * np.sin(x[j])
                
        # Chaotic saddle interactions with sine modulation
        saddle_sum = 0
        for i in range(self.dim):
            # Use chaotic sequence for varying saddle heights and depths
            saddle_height = 2.0 + 1.5 * self.chaos_seq[i]
            saddle_depth = 0.5 + 0.5 * np.sin(self.chaos_seq[i])
            saddle_val = (x[i]**2 - saddle_height)**2 + saddle_depth * np.cos(x[i])
            saddle_sum += saddle_val
            
        # Multi-modal sinusoidal modulation with chaotic frequencies
        modal_sum = 0
        for i in range(self.dim):
            freq = 1.5 + 2.5 * np.abs(self.chaos_seq[i])
            amp = 0.8 + 0.4 * np.sin(self.chaos_seq[i])
            modal_sum += amp * np.sin(freq * x[i]) * np.cos(0.3 * x[i])
            
        # Cross-terms with chaotic coupling coefficients
        cross_sum = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coeff = 0.2 + 0.8 * np.abs(self.chaos_seq[i])
                    cross_sum += coeff * x[i]**3 * x[j]
                    
        # Global scaling based on dimensionality
        scale_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return scale_factor * (poly_sum + rbf_sum + trig_sum + saddle_sum + modal_sum + cross_sum)