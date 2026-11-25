import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dynamic scaling
        r = np.sqrt(np.sum(x**2))
        result = 0.05 * r**2
        
        # Chaotic ridge structure with time-varying frequency
        ridge_freq = 3.0 + 1.5 * np.sin(0.3 * r)
        ridge_amp = 2.0 + 0.8 * np.cos(0.4 * r)
        
        for i in range(self.dim):
            # Dynamic ridge with chaotic modulation
            ridge_mod = 0.5 * np.sin(i * 0.7 + r * 0.2) * np.cos(x[i] * 0.3)
            result += ridge_amp * np.exp(-0.5 * (x[i] - ridge_freq * np.sin(ridge_mod))**2)
            
        # Asymmetric coupling terms with chaotic strength modulation
        for i in range(self.dim):
            coupling = 0.0
            for j in range(min(i+2, self.dim)):
                if i != j:
                    # Chaotic coupling strength
                    coupling_strength = 1.0 + 0.5 * np.sin(i * j * 0.3 + r * 0.1)
                    coupling += coupling_strength * (x[i] - x[j])**2 * np.exp(-0.1 * (x[i] - x[j])**2)
            result += 0.3 * coupling
            
        # Time-varying harmonic interference with dynamic phase shifts
        for i in range(self.dim):
            phase_shift = 0.5 * np.sin(i * 0.6 + r * 0.15)
            freq = 2.0 + 0.7 * np.cos(i * 0.4 + r * 0.2)
            result += 1.2 * np.sin(freq * x[i] + phase_shift) * np.cos(freq * x[i] * 0.3 + phase_shift)
            
        # Multi-scale chaotic barrier with dynamic positioning
        for i in range(self.dim):
            barrier_pos = 4.0 * np.sin(i * 0.5 + r * 0.1) * np.cos(x[i] * 0.2)
            barrier_height = 1.5 + 0.6 * np.sin(i * 0.3 + r * 0.25)
            distance = np.abs(x[i] - barrier_pos)
            if distance < 1.0:
                result += barrier_height * (1.0 + 0.8 * np.sin(10 * distance))
                
        # Asymmetric exponential penalty with chaotic scaling
        penalty_scale = 1.2 + 0.4 * np.sin(r * 0.3)
        for i in range(self.dim):
            result += penalty_scale * np.exp(2.0 * np.abs(x[i]) / 5.0) * (1.0 + 0.3 * np.sin(i * 0.5 + r * 0.2))
            
        # Dynamic harmonic interference with chaotic frequency modulation
        chaos_freq = 1.0 + 0.5 * np.sin(r * 0.4)
        for i in range(self.dim):
            result += 0.6 * np.sin(chaos_freq * x[i] + 0.3 * np.cos(i * 0.8)) * np.cos(0.7 * x[i] + 0.2 * np.sin(i * 0.6))
            
        return result