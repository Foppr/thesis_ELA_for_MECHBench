import numpy as np

class ChaoticRadialFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Base radial basis with chaotic modulation
        result = 0.0
        for i in range(self.dim):
            r = np.sqrt(np.sum(x**2)) + 1e-8
            radial_term = np.exp(-0.5 * (x[i] / (r + 1e-8))**2) * np.sin(r * (i + 1))
            result += 0.3 * radial_term
            
        # Enhanced chaotic gradient components with dynamic scaling
        for i in range(self.dim):
            grad_component = (x[i]**2 - 2*x[i]*np.sin(i) + np.sin(i)**2) * np.exp(-0.15 * abs(x[i]))
            result += 0.4 * grad_component
            
        # Self-interacting sinusoidal terms with frequency modulation and amplitude control
        for i in range(self.dim):
            freq_mod = 3.0 + 2.0 * np.sin(i * 0.8)
            amp_mod = 1.5 + 0.8 * np.cos(i * 0.6)
            sin_term = amp_mod * np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i] * 0.3)
            result += 0.25 * sin_term
            
        # Multi-scale interaction terms with exponential decay and chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                chaos_coupling = 1.0 + 0.5 * np.sin(i * j * 0.4)
                decay = np.exp(-0.25 * (x[i] - x[j])**2) * chaos_coupling
                result += 0.3 * interaction * decay
                
        # Polynomial chaos with cross-dimensional coupling and variable coupling strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.7 + 0.3 * np.cos(i * j * 0.3)
                poly_coupling = (x[i]**4) * (x[j]**2) + (x[j]**4) * (x[i]**2)
                result += coupling_strength * poly_coupling * np.exp(-0.1 * abs(x[i] - x[j]))
                
        # Adaptive basin terms with varying depths and chaotic basins
        for i in range(self.dim):
            basin = (x[i] - np.cos(i))**4 + 0.6 * (x[i] + np.sin(i))**3
            chaos_basin = 1.0 + 0.4 * np.sin(i * 2.0)
            result += 0.25 * basin * np.exp(-0.15 * abs(x[i])) * chaos_basin
            
        # High-frequency chaotic modulation with multi-exponential envelope
        for i in range(self.dim):
            chaos_freq = 10.0 + 4.0 * np.sin(i * 0.4)
            chaos_mod = np.sin(chaos_freq * x[i]) * np.cos(chaos_freq * x[i] * 0.9)
            envelope1 = np.exp(-x[i]**2 / 8.0)
            envelope2 = np.exp(-x[i]**2 / 15.0)
            result += 0.35 * chaos_mod * (envelope1 + 0.5 * envelope2)
            
        # Multi-modal landscape with variable amplitude sinusoids and chaotic amplitude modulation
        for i in range(self.dim):
            amp = 1.2 + 0.6 * np.sin(i * 1.5)
            freq = 4.0 + 3.0 * np.cos(i * 0.7)
            chaos_amp = 1.0 + 0.3 * np.sin(i * 2.5)
            result += amp * chaos_amp * np.sin(freq * x[i])**3
            
        # Cross-dimensional polynomial with varying coupling strength and chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.6 + 0.4 * np.sin(i * j * 0.3)
                poly_interaction = (x[i]**2) * (x[j]**4) + (x[j]**2) * (x[i]**4)
                chaos_mod = 1.0 + 0.5 * np.cos(i * j * 0.6)
                result += coupling_strength * poly_interaction * np.exp(-0.2 * abs(x[i] - x[j])) * chaos_mod
                
        # Dynamic curvature adjustment with time-varying parameters and chaotic modulation
        curvature = 0.0
        for i in range(self.dim):
            curvature += (x[i] - np.sin(i * 0.7))**2 * (1.0 + 0.4 * np.cos(i * 0.8))
        result += 0.15 * curvature
        
        # Additional chaotic penalty terms to increase landscape complexity
        penalty = 0.0
        for i in range(self.dim):
            penalty += 10.0 * np.exp(-0.1 * (x[i] - 3)**2) + 5.0 * np.exp(-0.1 * (x[i] + 3)**2)
        result += 0.2 * penalty
        
        return result