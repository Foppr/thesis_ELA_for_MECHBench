import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Fractal-like self-similarity component with chaotic scaling
        fractal_term = 0.0
        for i in range(self.dim):
            # Use a logistic map-like function for chaotic behavior
            chaotic_factor = 4 * x_scaled[i] * (1 - x_scaled[i])
            fractal_term += np.sin(2 * np.pi * chaotic_factor * 10) * np.cos(3 * np.pi * chaotic_factor * 7)
            
        # Dynamic landscape scaling based on coordinate interactions
        scale_factor = 1.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Interaction between dimensions creates dynamic scaling
                interaction = np.sin(x[i] * x[j] * 0.5) + 0.5 * np.cos(x[i] * x[j] * 2)
                scale_factor *= (1 + 0.3 * interaction)
                
        # Multimodal component with multiple peaks and varying frequencies
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += (np.sin(5 * x[i]) + 
                           0.6 * np.sin(12 * x[i]) + 
                           0.3 * np.cos(8 * x[i]) + 
                           0.2 * np.sin(15 * x[i]) +
                           0.1 * np.cos(10 * x[i]))
            
        # Cross-terms with fractal-like interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like interaction terms
                cross_term += (np.sin(x[i] * x[j]) + 
                              0.4 * np.cos(x[i] * x[j] * 3) + 
                              0.2 * np.sin(x[i] * x[j] * 7) +
                              0.1 * np.cos(x[i] * x[j] * 11)) * (i + j + 1)
                
        # Chaotic gradient modulation
        grad_mod = 1.0
        for i in range(self.dim):
            # Apply chaotic modulation to each dimension's contribution
            chaotic_val = np.sin(2 * np.pi * x[i] * 3) * np.cos(np.pi * x[i] * 5)
            grad_mod *= (1 + 0.4 * chaotic_val)
            
        # Self-similar structure with multiple scales
        self_similar = 0.0
        for i in range(self.dim):
            self_similar += (np.sin(x[i] * 2) + 
                            0.5 * np.sin(x[i] * 4) + 
                            0.2 * np.cos(x[i] * 8) + 
                            0.1 * np.sin(x[i] * 16))
            
        # Add a dynamic noise component that varies with the landscape
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(7 * x[i]) * np.cos(5 * x[i])
            
        # Combine all components with appropriate scaling
        result = (fractal_term + 
                 scale_factor * multi_modal + 
                 cross_term + 
                 grad_mod * self_similar + 
                 0.5 * noise)
        
        # Normalize and shift to ensure global minimum at origin
        return result + 2.5 * self.dim