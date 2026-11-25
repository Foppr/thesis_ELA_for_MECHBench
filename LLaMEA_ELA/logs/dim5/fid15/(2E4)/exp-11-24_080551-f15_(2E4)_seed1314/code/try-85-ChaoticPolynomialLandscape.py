import numpy as np

class ChaoticPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Base polynomial landscape with mixed degrees
        result = 0.0
        for i in range(self.dim):
            result += 0.5 * x[i]**4 + 0.3 * x[i]**3 - 0.8 * x[i]**2 + 0.1 * x[i]
            
        # Chaotic sinusoidal modulations with dynamic frequencies
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(x[i] * 0.5)
            result += 0.7 * np.sin(freq * x[i]) * np.cos(1.5 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Cross-dimensional polynomial coupling with variable exponents
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exponent = 1.0 + 0.5 * np.sin(i * j * 0.3)
                coupling = (x[i]**exponent) * (x[j]**(3.0 - exponent))
                result += 0.25 * coupling * np.exp(-0.05 * abs(x[i] - x[j]))
                
        # Adaptive basin structure with time-varying depth
        for i in range(self.dim):
            basin_depth = 1.0 + 0.5 * np.cos(i * 0.8)
            result += basin_depth * np.exp(-0.5 * (x[i] - np.sin(i * 0.7))**2) * np.sin(2.0 * x[i])
            
        # High-frequency oscillatory terms with varying amplitudes
        for i in range(self.dim):
            amplitude = 0.8 + 0.3 * np.sin(i * 1.2)
            result += amplitude * np.sin(10.0 * x[i]) * np.cos(8.0 * x[i]) * np.exp(-0.2 * abs(x[i]))
            
        # Multi-scale chaotic interactions with exponential decay
        for i in range(self.dim):
            chaotic_sum = 0.0
            for k in range(1, 6):
                chaotic_sum += np.sin(k * x[i] + k * np.cos(i * 0.5)) / k
            result += 0.4 * chaotic_sum * np.exp(-0.3 * x[i]**2)
            
        # Asymmetric cubic interactions with varying coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.5 + 0.3 * np.sin(i * j * 0.4)
                interaction = (x[i]**3) * (x[j]**2) + (x[j]**3) * (x[i]**2)
                result += strength * interaction * np.exp(-0.1 * abs(x[i] - x[j]))
                
        # Central repulsion with variable influence range
        center_dist = np.sqrt(np.sum(x**2))
        if center_dist > 0:
            result += 1.5 * np.exp(-center_dist**2 / 2.0) * np.sin(center_dist * 2.0)
            
        # Boundary penalty with adaptive strength
        boundary_penalty = 0.0
        for i in range(self.dim):
            if x[i] < -4.5 or x[i] > 4.5:
                boundary_penalty += 2.0 * (abs(x[i]) - 4.5)**2
        result += boundary_penalty
        
        return result