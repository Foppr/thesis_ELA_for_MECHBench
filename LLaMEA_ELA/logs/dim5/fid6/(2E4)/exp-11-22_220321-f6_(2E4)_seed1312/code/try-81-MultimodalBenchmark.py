import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.alpha = 0.8
        self.beta = 2.5
        self.gamma = 1.8
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with asymmetric scaling and frequency modulation
        result = 0.0
        for i in range(self.dim):
            freq_mod = 1 + 0.3 * np.sin(i * 0.4)
            result += (x[i] ** 2) * freq_mod
            
        # Enhanced sine-wave interaction terms with chaotic modulations
        sine_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 1 + 0.2 * np.sin(i * 0.6)
                freq_j = 1 + 0.2 * np.sin(j * 0.6)
                sine_interaction += np.sin(freq_i * x[i] * freq_j * x[j]) * np.cos(self.beta * (x[i] + x[j]))
                
        # Polynomial chaos component with dynamic weights and adaptive scaling
        chaos_term = 0.0
        for i in range(self.dim):
            scale_factor = 1 + 0.2 * np.sin(i * 0.5)
            chaos_term += (x[i]**4 + self.gamma * x[i]**6) * np.exp(-0.15 * x[i]**2) * scale_factor
            
        # Dynamic cross-dimensional coupling with varying strength and chaotic phases
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_shift = np.sin(0.7 * i * j)
                coupling += (x[i] * x[j]) * np.sin(1.8 * np.pi * (x[i] - x[j]) + phase_shift) * \
                           (1 + 0.4 * np.cos(i * j * 0.5))
                           
        # Non-convex penalty with enhanced polynomial terms and adaptive coefficients
        penalty = 0.0
        for i in range(self.dim):
            adaptive_coeff = 1 + 0.3 * np.sin(i * 0.4)
            penalty += (x[i]**9 + x[i]**5 + x[i]**3) * adaptive_coeff
            
        # Fractional polynomial penalties with nested trigonometric cascades
        fractional_penalty = 0.0
        for i in range(self.dim):
            frac_exp = 1.5 + 0.5 * np.sin(i * 0.8)
            fractional_penalty += (np.abs(x[i]) ** frac_exp) * np.cos(2 * np.pi * x[i])
            
        # Adaptive radial basis functions with dynamic coupling strengths
        rbf_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                rbf_strength = 1 + 0.3 * np.sin(i * j * 0.7)
                rbf_term += rbf_strength * np.exp(-dist**2 / (2 * (0.5 + 0.2 * np.sin(i + j))))
                
        # Add a global modulation factor to increase landscape complexity
        modulation_factor = 1 + 0.1 * np.sin(np.sum(x) * 0.3)
        
        return modulation_factor * (result + 0.4 * sine_interaction + 0.3 * chaos_term + 0.25 * coupling + 0.4 * penalty + 0.3 * fractional_penalty + 0.2 * rbf_term)