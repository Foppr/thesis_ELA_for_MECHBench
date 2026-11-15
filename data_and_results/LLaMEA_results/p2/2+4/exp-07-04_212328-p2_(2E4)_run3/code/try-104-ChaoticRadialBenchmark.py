import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Base quadratic term with conditioning
        f = 0.5 * np.sum(x**2)
        
        # Add radial basis functions with chaotic centers
        rbf_sum = 0
        centers = []
        for i in range(15):
            center = np.array([np.sin(i * 0.7) * 4.0, np.cos(i * 0.7) * 4.0])
            if self.dim >= 2:
                diff = x[:2] - center
                rbf_sum += np.exp(-0.5 * np.sum(diff**2) / (0.5 + 0.3 * np.sin(i * 0.3)))
        
        f += 2.0 * rbf_sum
        
        # Add adaptive frequency modulation based on input values
        freq_mod = 0
        for i in range(self.dim):
            freq_mod += np.sin(x[i] * (1 + 0.5 * np.sin(x[i] * 0.3))) * np.cos(x[i] * (1 + 0.3 * np.cos(x[i] * 0.2)))
        f += 0.8 * freq_mod
        
        # Add multi-scale sinusoidal coupling with dynamic amplitudes
        coupling_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                amp = 0.5 + 0.3 * np.sin(x[i] * 0.5) * np.cos(x[j] * 0.4)
                coupling_sum += amp * np.sin(x[i] * x[j] * 0.8 + 0.5 * np.sin(x[i] + x[j]))
        f += 1.2 * coupling_sum
        
        # Add chaotic phase interactions with recursive structure
        phase_sum = 0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] + np.sin(x[i] * 1.5) + np.sin(x[i] * 0.7))
        f += 0.6 * np.sin(phase_sum * 2.0)
        
        # Add polynomial chaos with non-linear coupling
        poly_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_sum += (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j] * 0.5)
        f += 0.4 * poly_sum
        
        # Add multiple global minima with varying distances and scales
        minima_positions = []
        for i in range(10):
            minima_positions.append([np.sin(i * 0.6) * 3.0, np.cos(i * 0.6) * 3.0])
            minima_positions.append([np.sin(i * 0.8) * 2.0, np.cos(i * 0.8) * 2.0])
            
        minima_sum = 0
        for pos in minima_positions:
            if self.dim >= len(pos):
                diff = x[:len(pos)] - np.array(pos)
                minima_sum += np.exp(-0.3 * np.sum(diff**2))
        f += 1.5 * minima_sum
        
        # Add noise with chaotic pattern
        noise = 0
        for i in range(self.dim):
            noise += np.sin(x[i] * 10.0 + np.sin(x[i] * 7.0)) * np.cos(x[i] * 5.0)
        f += 0.1 * noise
        
        return f