import numpy as np

class FractalTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.exp_base = 1.5
        self.trig_freq = 3.0
        self.fractal_dim = 1.7
        self.conditioning_factor = 2.0
        self.oscillation_amplitude = 0.8
        self.self_similarity_scale = 0.3
        self.rotation_angles = np.random.uniform(-np.pi, np.pi, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential component with dynamic base
        exp_term = 0.0
        for i in range(self.dim):
            base = self.exp_base * (1.0 + 0.3 * np.sin(i * 0.4))
            exp_term += np.exp(base * np.abs(x[i])) * np.cos(0.5 * x[i])
            
        # Trigonometric component with varying frequencies
        trig_term = 0.0
        for i in range(self.dim):
            freq = self.trig_freq * (1.0 + 0.2 * np.sin(i * 0.6))
            trig_term += np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Fractal-like self-similar structure
        fractal_term = 0.0
        for i in range(self.dim):
            # Create self-similar pattern using multiple scales
            scale_factor = self.self_similarity_scale
            for j in range(3):  # Three levels of self-similarity
                scaled_x = x[i] * (scale_factor ** j)
                fractal_term += np.sin(scaled_x) * np.cos(scaled_x) * (scale_factor ** (j * self.fractal_dim))
                
        # Cross-dimensional coupling with rotation
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                rotated_i = x[i] * np.cos(self.rotation_angles[i]) - x[j] * np.sin(self.rotation_angles[i])
                rotated_j = x[i] * np.sin(self.rotation_angles[j]) + x[j] * np.cos(self.rotation_angles[j])
                cross_term += np.sin(rotated_i + rotated_j) * np.cos(0.5 * (rotated_i - rotated_j))
                
        # Dynamic conditioning with oscillation
        cond_term = 0.0
        for i in range(self.dim):
            oscillation = self.oscillation_amplitude * np.sin(i * 0.8 + x[i])
            condition_factor = self.conditioning_factor * (1.0 + 0.5 * oscillation)
            cond_term += condition_factor * x[i]**3
            
        # Combined fitness function
        total = exp_term + trig_term + fractal_term + cross_term + cond_term
        
        return total