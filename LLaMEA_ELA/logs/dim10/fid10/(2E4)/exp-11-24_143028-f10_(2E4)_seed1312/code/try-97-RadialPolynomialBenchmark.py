import numpy as np

class RadialPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base radial term with quartic decay
        result = 0.3 * np.sum(x**4) * np.exp(-0.15 * np.sum(x**2))
        
        # Multi-frequency polynomial oscillations
        for i in range(self.dim):
            result += 2.5 * x[i]**5 * np.sin(12 * x[i]) * np.cos(9 * x[i]) * np.tan(7 * x[i])
        
        # Radial basis function components with varying widths and phases
        for i in range(self.dim):
            result += 2.0 * np.exp(-0.4 * (x[i] - 2.5)**2) + 1.5 * np.exp(-0.2 * (x[i] + 3.5)**2) + 1.0 * np.exp(-0.6 * (x[i] - 1.0)**2)
        
        # Asymmetric boundary penalties with complex waveforms
        for i in range(self.dim):
            if x[i] < 0:
                result += 4.0 * np.exp(-0.4 * (x[i] + 5.0)**2) * (1 + 0.6 * np.sin(18 * x[i]) + 0.3 * np.cos(25 * x[i]))
            else:
                result += 3.5 * np.exp(-0.2 * (x[i] - 5.0)**2) * (1 + 0.5 * np.cos(14 * x[i]) + 0.4 * np.sin(20 * x[i]))
        
        # Coupling between dimensions with complex sine modulation and phase shifts
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                coupling = 1.0 + 0.4 * np.sin(6 * (x[i] + x[j]) + 0.5) * np.cos(4 * (x[i] - x[j]) + 1.2)
                result += coupling * np.sin(8 * x[i]) * np.cos(10 * x[j]) * np.exp(-0.3 * (x[i] - x[j])**2)
        
        # High-frequency chaotic modulation with multiple sine components
        chaos_factor = 1.0
        for i in range(self.dim):
            chaos_factor *= np.sin(15 * x[i]) + 1.8 * np.cos(11 * x[i]) + 1.2
        result += 1.5 * chaos_factor
        
        # Fractal-like structure with recursive sine and cosine components
        for i in range(self.dim):
            result += 1.0 * np.sin(25 * x[i]) * np.cos(22 * x[i]) * np.sin(19 * x[i]**2) * np.cos(17 * x[i]**3) * (1 + 0.4 * np.abs(x[i]))
        
        # Weighted sum of polynomial and trigonometric terms with dynamic coefficients
        poly_term = 0
        for i in range(self.dim):
            poly_term += 1.5 * x[i]**5 + 0.8 * x[i]**4 - 0.3 * x[i]**3 + 0.1 * x[i]**2
        result += 1.2 * poly_term * np.cos(6 * np.sum(x)) * np.sin(4 * np.sum(x)**2)
        
        # Cross-dimensional exponential interaction with variable decay rates
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.8 * np.exp(-np.abs(x[i] - x[j]) / (1 + 0.3 * np.abs(x[i] + x[j]) + 0.1 * np.abs(x[i] - x[j])**2)) * np.sin(12 * (x[i] + x[j])) * np.cos(8 * (x[i] - x[j]))
        
        # Additional asymmetric wave pattern with multiple frequencies
        sum_x = np.sum(x)
        result += 2.2 * np.sin(30 * sum_x) * np.cos(25 * sum_x) * np.tan(20 * sum_x) * (1 + 0.5 * np.tanh(sum_x) + 0.3 * np.sin(15 * sum_x))
        
        # Add a global minimum scaling factor
        result *= (1.0 + 0.1 * np.abs(np.sum(x**2) - self.dim))
        
        return result