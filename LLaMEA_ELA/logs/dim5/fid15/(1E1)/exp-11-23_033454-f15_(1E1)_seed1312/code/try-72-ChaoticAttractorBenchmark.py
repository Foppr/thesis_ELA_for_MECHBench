import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for different dimensions
        np.random.seed(42)
        self.chaos_params = np.random.uniform(0.1, 2.0, dim)
        self.oscillation_freq = np.random.uniform(0.5, 2.0, dim)
        self.attractor_positions = np.random.uniform(-3.0, 3.0, (5, dim))
        
    def f(self, x):
        if len(x) != self.dim:
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dimension-dependent conditioning
        base_term = 0.1 * np.sum(x**2)
        
        # Chaotic attractor component with time-varying dynamics
        chaotic_term = 0.0
        for i in range(5):  # 5 nested attractors
            dist = np.sum((x - self.attractor_positions[i])**2)
            attraction_strength = 1.0 / (1.0 + dist)
            # Add chaotic modulation based on dimension-specific parameters
            chaos_mod = np.prod(np.sin(self.chaos_params * x + i))
            chaotic_term += attraction_strength * np.abs(chaos_mod)
        
        # Oscillatory component with multi-frequency interaction
        oscillatory_term = 0.0
        for i in range(self.dim):
            # Multi-frequency oscillation with dimension-specific frequencies
            osc_val = 0.0
            for freq in self.oscillation_freq:
                osc_val += np.sin(freq * x[i] + freq * i)
            oscillatory_term += osc_val**2
        
        # Time-dependent dynamic component (using current iteration as time)
        dynamic_term = 0.0
        for i in range(self.dim):
            # Create a dynamic valley that shifts with dimension
            shift = np.sin(i * 0.5) * np.cos(x[i] * 0.3)
            dynamic_term += shift**2
        
        # Combine all terms with varying weights
        return base_term + 0.5 * chaotic_term + 0.3 * oscillatory_term + 0.2 * dynamic_term