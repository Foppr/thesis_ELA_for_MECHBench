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
        
        # Enhanced chaotic ridge structure with multi-scale modulation
        ridge_freq = 3.0 + 1.5 * np.sin(0.3 * r)
        ridge_amp = 2.0 + 0.8 * np.cos(0.4 * r)
        
        for i in range(self.dim):
            # Enhanced dynamic ridge with chaotic modulation and multi-scale interference
            ridge_mod = 0.5 * np.sin(i * 0.7 + r * 0.2) * np.cos(x[i] * 0.3)
            result += ridge_amp * np.exp(-0.5 * (x[i] - ridge_freq * np.sin(ridge_mod))**2)
            
        # Enhanced asymmetric coupling terms with chaotic strength modulation and multi-scale interactions
        for i in range(self.dim):
            coupling = 0.0
            for j in range(min(i+3, self.dim)):  # Extended coupling range
                if i != j:
                    # Chaotic coupling strength with enhanced modulation
                    coupling_strength = 1.0 + 0.5 * np.sin(i * j * 0.3 + r * 0.1) * np.cos(i * 0.2 + j * 0.1)
                    coupling += coupling_strength * (x[i] - x[j])**2 * np.exp(-0.1 * (x[i] - x[j])**2)
            result += 0.35 * coupling  # Slightly increased coupling weight
            
        # Enhanced time-varying harmonic interference with dynamic phase shifts and multi-scale frequencies
        for i in range(self.dim):
            phase_shift = 0.5 * np.sin(i * 0.6 + r * 0.15)
            freq = 2.0 + 0.7 * np.cos(i * 0.4 + r * 0.2)
            result += 1.3 * np.sin(freq * x[i] + phase_shift) * np.cos(freq * x[i] * 0.3 + phase_shift)
            
        # Enhanced multi-scale chaotic barrier with dynamic positioning and variable height
        for i in range(self.dim):
            barrier_pos = 4.0 * np.sin(i * 0.5 + r * 0.1) * np.cos(x[i] * 0.2)
            barrier_height = 1.5 + 0.6 * np.sin(i * 0.3 + r * 0.25) * np.cos(r * 0.1)
            distance = np.abs(x[i] - barrier_pos)
            if distance < 1.0:
                result += barrier_height * (1.0 + 0.8 * np.sin(10 * distance))
                
        # Enhanced asymmetric exponential penalty with chaotic scaling and multi-scale modulation
        penalty_scale = 1.2 + 0.4 * np.sin(r * 0.3) * np.cos(r * 0.1)
        for i in range(self.dim):
            result += penalty_scale * np.exp(2.0 * np.abs(x[i]) / 5.0) * (1.0 + 0.3 * np.sin(i * 0.5 + r * 0.2))
            
        # Enhanced dynamic harmonic interference with chaotic frequency modulation and multi-scale structure
        chaos_freq = 1.0 + 0.5 * np.sin(r * 0.4) * np.cos(r * 0.2)
        for i in range(self.dim):
            result += 0.65 * np.sin(chaos_freq * x[i] + 0.3 * np.cos(i * 0.8)) * np.cos(0.7 * x[i] + 0.2 * np.sin(i * 0.6))
            
        # Additional chaotic modulation to improve conditioning
        chaos_mod = 0.1 * np.sin(r * 0.5) * np.cos(r * 0.3)
        result += chaos_mod
        
        return result