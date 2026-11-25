import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Logistic map chaos parameter
        self.r = 3.95
        # Initialize chaotic sequence
        self.chaos_seq = self._initialize_chaos()
        
    def _initialize_chaos(self):
        # Generate chaotic sequence using logistic map
        seq = np.zeros(self.dim)
        x = 0.5
        for i in range(self.dim):
            x = self.r * x * (1 - x)
            seq[i] = x
        return seq
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial potential component
        poly_sum = 0
        for i in range(self.dim):
            poly_sum += (x[i]**4 + 0.5 * x[i]**3 + 2.0 * x[i]**2 + 0.1 * x[i])
            
        # Trigonometric coupling terms
        trig_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Coupling with chaotic weights
                weight = 0.5 + 0.5 * np.sin(self.chaos_seq[i] * self.chaos_seq[j])
                trig_sum += weight * np.sin(x[i]) * np.cos(x[j])
                
        # Chaotic saddle interactions
        saddle_sum = 0
        for i in range(self.dim):
            # Use chaotic sequence for varying saddle heights
            saddle_height = 1.5 + 2.0 * self.chaos_seq[i]
            saddle_val = (x[i]**2 - saddle_height)**2
            saddle_sum += saddle_val
            
        # Multi-modal sinusoidal modulation
        modal_sum = 0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(self.chaos_seq[i])
            amp = 1.0 + 0.5 * np.cos(self.chaos_seq[i])
            modal_sum += amp * np.sin(freq * x[i]) * np.cos(0.5 * x[i])
            
        # Cross-terms with chaotic coefficients
        cross_sum = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Use chaotic coefficient for coupling strength
                    coeff = 0.3 + 0.7 * self.chaos_seq[i]
                    cross_sum += coeff * x[i]**2 * x[j]**3
                    
        # Global scaling based on dimensionality
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        return scale_factor * (poly_sum + trig_sum + saddle_sum + modal_sum + cross_sum)