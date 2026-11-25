import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Chaotic ridge structure with dynamic frequency modulation
        for i in range(self.dim):
            # Dynamic frequency based on position and dimension
            freq = 2.0 + 1.5 * np.sin(i * 0.5 + np.sum(x) * 0.1)
            # Ridge term with chaotic amplitude modulation
            amp = 1.0 + 0.5 * np.cos(i * 0.3 + np.sum(x**2) * 0.05)
            result += amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Asymmetric coupling terms with time-varying strength
        for i in range(self.dim):
            coupling = 0.0
            for j in range(min(i+3, self.dim)):
                if i != j:
                    # Time-varying coupling strength
                    coupling_strength = 0.5 + 0.3 * np.sin(i * j * 0.2 + np.sum(x) * 0.1)
                    coupling += coupling_strength * (x[i] - x[j])**2 * np.cos(0.5 * (x[i] + x[j]))
            result += 0.2 * coupling
            
        # Multi-scale harmonic interference with chaotic phase shifts
        for i in range(self.dim):
            scale = 2**(i % 4) * (1.0 + 0.2 * np.sin(i * 0.3))
            phase_shift = 0.5 * np.sin(i * 0.4 + np.sum(x) * 0.15)
            result += 0.8 * np.sin(scale * x[i] + phase_shift) * np.cos(scale * x[i] * 0.25 + phase_shift)
            
        # Dynamic barrier penalties with chaotic positioning
        for i in range(self.dim):
            # Chaotic barrier position
            barrier_pos = 4.0 * np.sin(i * 0.6 + np.sum(x) * 0.1)
            distance = np.abs(np.abs(x[i]) - np.abs(barrier_pos))
            if distance < 1.5:
                # Time-varying barrier height
                barrier_height = 2.0 + 1.0 * np.cos(i * 0.3 + np.sum(x) * 0.2)
                result += barrier_height * (distance / (1.5 - distance))**2
                
        # Exponential penalty with asymmetric scaling
        for i in range(self.dim):
            # Asymmetric scaling based on sign of variable
            scale = 1.5 + 0.8 * np.sin(i * 0.4 + np.sum(x) * 0.1)
            if x[i] > 0:
                result += scale * np.exp(0.5 * x[i])
            else:
                result += scale * np.exp(0.3 * x[i])
                
        # Time-varying harmonic interference
        time_factor = 0.2 * np.sin(np.sum(x) * 0.1)
        for i in range(self.dim):
            result += 0.4 * np.sin(5.0 * x[i] + time_factor) * np.cos(3.0 * x[i] + time_factor)
            
        return result