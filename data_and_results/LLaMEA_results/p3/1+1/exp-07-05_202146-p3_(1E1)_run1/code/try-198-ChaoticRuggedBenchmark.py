import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_coeffs = np.array([np.sin(i * 0.73) * np.cos(i * 0.91) for i in range(dim)])
        self.history = np.zeros(dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = np.sum(x**2)
        
        # Enhanced chaotic ruggedness with double sine modulation
        for i in range(self.dim):
            result += 1.2 * np.sin(3.1 * x[i])**2 * np.cos(2.7 * x[i]) * np.exp(-0.15 * np.abs(x[i]))
            
        # Multi-scale phase interactions with dynamic coupling
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.12 * i)) * np.cos(x[i] * 0.31)
        result += 0.85 * np.sin(phase_sum * 1.4) * np.cos(phase_sum * 0.89)
        
        # Complex cross-dimensional interactions with time-varying weights
        time_weight = np.sin(np.sum(x) * 0.23) + 1.5
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.06 * (i + j))
                interaction = x[i] * x[j] * np.sin(x[i] + x[j] * time_weight)
                result += decay * interaction * time_weight
                
        # High-order non-separable terms with varying exponents
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.15 * x[i]**1.7 * x[j]**2.3 * x[k]**1.2 * np.sin(x[i] * x[j] * x[k] * 0.5)
                    
        # Fractal self-similarity with recursive scaling
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_coeffs[i] * np.sin(4.2 * x[i]) * np.cos(2.1 * x[i]) * np.exp(-0.08 * np.abs(x[i]))
        result += 0.22 * fractal_term
        
        # Memory-dependent basin structure with historical influence
        hist_influence = 0.0
        for i in range(self.dim):
            hist_influence += 0.11 * self.history[i] * np.sin(x[i] * 0.73) * np.cos(x[i] * 0.41)
        result += hist_influence
        
        # Multi-modal landscape with asymmetric peaks
        for i in range(self.dim):
            result += 0.27 * np.sin(15.6 * x[i]) * np.cos(7.8 * x[i]) * np.exp(-0.023 * x[i]**2)
            
        # Dynamic basin boundaries with chaotic attractors
        basin_term = 0.0
        for i in range(self.dim):
            basin_term += 0.18 * np.sin(9.3 * x[i]) * np.cos(4.65 * x[i]) * np.exp(-0.031 * np.abs(x[i]))
        result += basin_term
        
        # Enhanced noise with multi-frequency components
        noise = 0.0
        for i in range(self.dim):
            noise += 0.42 * np.sin(14.7 * x[i]) * np.cos(7.35 * x[i]) * np.exp(-0.073 * i)
        result += noise
        
        # Global minimum enforcing with logarithmic penalty and exponential scaling
        result += 0.035 * np.sum(np.log(1.0 + np.abs(x))) * np.exp(-0.01 * np.sum(x**2))
        
        # Complex oscillatory structure with variable amplitude
        for i in range(self.dim):
            amp = 1.5 + 0.6 * np.sin(i * 0.53)
            freq = 2.3 + 3.7 * np.cos(i * 0.41)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.67)
            
        # Memory effect with cumulative influence
        cumulative_influence = 0.0
        for i in range(self.dim):
            cumulative_influence += 0.08 * np.sin(x[i] * 0.92) * np.cos(x[i] * 0.46) * np.exp(-0.005 * np.sum(x**2))
        result += cumulative_influence
        
        # Update history for next iteration
        self.history = x.copy()
        
        return result