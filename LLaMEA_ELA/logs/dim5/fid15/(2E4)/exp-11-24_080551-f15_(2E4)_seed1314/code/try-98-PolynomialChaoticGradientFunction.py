import numpy as np

class PolynomialChaoticGradientFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Base polynomial chaos expansion with varying exponents
        result = 0.0
        for i in range(self.dim):
            poly_term = (x[i]**(i % 4 + 2)) * np.cos(x[i] * (i + 1))
            result += 0.5 * poly_term
            
        # Adaptive gradient-like components with dynamic scaling
        for i in range(self.dim):
            grad_component = (x[i] - np.sin(i))**2 * np.exp(-0.1 * abs(x[i]))
            result += 0.3 * grad_component
            
        # Self-interacting sinusoidal terms with frequency modulation
        for i in range(self.dim):
            freq_mod = 2.0 + 1.5 * np.sin(i * 0.7)
            sin_term = np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i] * 0.5)
            result += 0.4 * sin_term
            
        # Multi-scale interaction terms with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                decay = np.exp(-0.2 * (x[i] - x[j])**2)
                result += 0.25 * interaction * decay
                
        # Polynomial chaos with cross-dimensional coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling = (x[i]**3) * (x[j]**2) + (x[j]**3) * (x[i]**2)
                result += 0.15 * poly_coupling * np.exp(-0.1 * abs(x[i] - x[j]))
                
        # Adaptive basin terms with varying depths
        for i in range(self.dim):
            basin = (x[i] - np.cos(i))**4 + 0.5 * (x[i] + np.sin(i))**3
            result += 0.2 * basin * np.exp(-0.1 * abs(x[i]))
            
        # High-frequency chaotic modulation with exponential envelope
        for i in range(self.dim):
            chaos_freq = 8.0 + 3.0 * np.sin(i * 0.3)
            chaos_mod = np.sin(chaos_freq * x[i]) * np.cos(chaos_freq * x[i] * 0.8)
            envelope = np.exp(-x[i]**2 / 10.0)
            result += 0.3 * chaos_mod * envelope
            
        # Multi-modal landscape with variable amplitude sinusoids
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(i * 1.3)
            freq = 3.0 + 2.0 * np.cos(i * 0.6)
            result += amp * np.sin(freq * x[i])**4
            
        # Cross-dimensional polynomial with varying coupling strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.5 + 0.3 * np.sin(i * j * 0.2)
                poly_interaction = (x[i]**2) * (x[j]**3) + (x[j]**2) * (x[i]**3)
                result += coupling_strength * poly_interaction * np.exp(-0.15 * abs(x[i] - x[j]))
                
        # Dynamic curvature adjustment with time-varying parameters
        curvature = 0.0
        for i in range(self.dim):
            curvature += (x[i] - np.sin(i * 0.5))**2 * (1.0 + 0.3 * np.cos(i))
        result += 0.1 * curvature
        
        return result