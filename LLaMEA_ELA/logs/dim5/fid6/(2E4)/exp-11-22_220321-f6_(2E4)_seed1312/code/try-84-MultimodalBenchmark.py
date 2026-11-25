import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.alpha = 0.85
        self.beta = 2.7
        self.gamma = 1.9
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with asymmetric scaling and frequency modulation
        result = 0.0
        for i in range(self.dim):
            freq_mod = 1 + 0.32 * np.sin(i * 0.43)
            result += (x[i] ** 2) * freq_mod
            
        # Enhanced sine-wave interaction terms with chaotic modulations
        sine_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 1 + 0.21 * np.sin(i * 0.62)
                freq_j = 1 + 0.21 * np.sin(j * 0.62)
                sine_interaction += np.sin(freq_i * x[i] * freq_j * x[j]) * np.cos(self.beta * (x[i] + x[j]))
                
        # Polynomial chaos component with dynamic weights and adaptive scaling
        chaos_term = 0.0
        for i in range(self.dim):
            scale_factor = 1 + 0.21 * np.sin(i * 0.53)
            chaos_term += (x[i]**4 + self.gamma * x[i]**6) * np.exp(-0.16 * x[i]**2) * scale_factor
            
        # Dynamic cross-dimensional coupling with varying strength and chaotic phases
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_shift = np.sin(0.73 * i * j)
                coupling += (x[i] * x[j]) * np.sin(1.85 * np.pi * (x[i] - x[j]) + phase_shift) * \
                           (1 + 0.41 * np.cos(i * j * 0.52))
                           
        # Non-convex penalty with enhanced polynomial terms and adaptive coefficients
        penalty = 0.0
        for i in range(self.dim):
            adaptive_coeff = 1 + 0.31 * np.sin(i * 0.42)
            penalty += (x[i]**9 + x[i]**5 + x[i]**3) * adaptive_coeff
            
        # Fractional polynomial penalties with nested trigonometric cascades
        fractional_penalty = 0.0
        for i in range(self.dim):
            frac_exp = 1.52 + 0.48 * np.sin(i * 0.82)
            fractional_penalty += (np.abs(x[i]) ** frac_exp) * np.cos(2.05 * np.pi * x[i])
            
        # Adaptive radial basis functions with dynamic coupling strengths
        rbf_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.11)
                rbf_strength = 1 + 0.31 * np.sin(i * j * 0.72)
                rbf_term += rbf_strength * np.exp(-dist**2 / (2 * (0.51 + 0.21 * np.sin(i + j))))
                
        # Add a global modulation factor to increase landscape complexity
        modulation_factor = 1 + 0.105 * np.sin(np.sum(x) * 0.31)
        
        return modulation_factor * (result + 0.41 * sine_interaction + 0.31 * chaos_term + 0.26 * coupling + 0.41 * penalty + 0.31 * fractional_penalty + 0.21 * rbf_term)