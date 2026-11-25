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
        
        # Polynomial potential component with fractal-like scaling
        poly_sum = 0
        for i in range(self.dim):
            poly_sum += (x[i]**4 + 0.5 * x[i]**3 + 2.0 * x[i]**2 + 0.1 * x[i]) * (1.0 + 0.1 * np.sin(10 * self.chaos_seq[i]))
            
        # Trigonometric coupling terms with dynamic weights
        trig_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic weight based on chaotic sequence and distance
                dist = np.abs(x[i] - x[j])
                weight = (0.5 + 0.5 * np.sin(self.chaos_seq[i] * self.chaos_seq[j])) * (1.0 + 0.2 * np.cos(dist))
                trig_sum += weight * np.sin(x[i]) * np.cos(x[j])
                
        # Chaotic saddle interactions with multi-scale heights
        saddle_sum = 0
        for i in range(self.dim):
            # Multi-scale saddle heights using chaotic sequence
            saddle_height = 1.5 + 2.0 * self.chaos_seq[i] + 0.5 * np.sin(5 * self.chaos_seq[i])
            saddle_val = (x[i]**2 - saddle_height)**2
            saddle_sum += saddle_val
            
        # Multi-modal sinusoidal modulation with dynamic frequencies
        modal_sum = 0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(self.chaos_seq[i]) + 0.5 * np.cos(2 * self.chaos_seq[i])
            amp = 1.0 + 0.5 * np.cos(self.chaos_seq[i]) * (1.0 + 0.1 * np.sin(7 * self.chaos_seq[i]))
            modal_sum += amp * np.sin(freq * x[i]) * np.cos(0.5 * x[i])
            
        # Cross-terms with fractal-like coefficients
        cross_sum = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Fractal coefficient based on chaotic sequence and dimension
                    coeff = (0.3 + 0.7 * self.chaos_seq[i]) * (1.0 + 0.2 * np.sin(self.dim * self.chaos_seq[j]))
                    cross_sum += coeff * x[i]**2 * x[j]**3
                    
        # Self-similarity pattern with multiple scales
        self_sim = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                scale = 1.0 + 0.3 * np.sin(3 * self.chaos_seq[i] * self.chaos_seq[j])
                self_sim += scale * np.exp(-dist**2 / (2 * 0.5**2))
                
        # Global scaling based on dimensionality and chaos
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1) + 0.05 * np.sin(self.chaos_seq[0])
        
        return scale_factor * (poly_sum + trig_sum + saddle_sum + modal_sum + cross_sum + 0.5 * self_sim)