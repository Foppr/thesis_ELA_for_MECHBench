import numpy as np

class ChaoticRadialPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base radial term with quintic decay and dynamic conditioning
        result = 0.4 * np.sum(x**5) * np.exp(-0.2 * np.sum(x**2))
        
        # Multi-frequency polynomial oscillations with chaotic modulation
        for i in range(self.dim):
            result += 2.1 * x[i]**6 * np.sin(15 * x[i]) * np.cos(11 * x[i]) * (1 + 0.3 * np.sin(23 * x[i]))
        
        # Radial basis function components with varying widths, phases, and chaotic offsets
        for i in range(self.dim):
            result += 2.5 * np.exp(-0.5 * (x[i] - 2.8)**2) + 1.5 * np.exp(-0.3 * (x[i] + 3.8)**2) + 1.0 * np.exp(-0.7 * (x[i] - 1.3)**2)
        
        # Asymmetric boundary penalties with higher-order polynomial terms and chaotic sine waves
        for i in range(self.dim):
            if x[i] < 0:
                result += 3.2 * np.exp(-0.5 * (x[i] + 5.0)**4) * (1 + 0.7 * np.sin(20 * x[i]) + 0.4 * np.cos(15 * x[i]))
            else:
                result += 2.6 * np.exp(-0.3 * (x[i] - 5.0)**4) * (1 + 0.6 * np.cos(16 * x[i]) + 0.3 * np.sin(19 * x[i]))
        
        # Coupling between dimensions with multiple cosine modulations and exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = 1.1 + 0.5 * np.cos(7 * (x[i] - x[j])) + 0.3 * np.sin(9 * (x[i] + x[j]))
                result += coupling * np.cos(9 * x[i]) * np.sin(12 * x[j]) * np.exp(-0.2 * (x[i] + x[j])**2)
        
        # High-frequency chaotic modulation with multiple sine and cosine waves
        chaos_factor = 1.2
        for i in range(self.dim):
            chaos_factor *= np.sin(18 * x[i]) + np.cos(20 * x[i]) + 2.1 + 0.5 * np.sin(25 * x[i])
        result += 1.8 * chaos_factor
        
        # Fractal-like structure with recursive cosine and polynomial components
        for i in range(self.dim):
            result += 1.3 * np.cos(30 * x[i]) * np.sin(25 * x[i]) * np.cos(25 * x[i]**2) * (1 + 0.5 * np.abs(x[i])) * np.exp(-0.1 * x[i]**3)
        
        # Weighted sum of polynomial and trigonometric terms with quintic interaction
        poly_term = 0
        for i in range(self.dim):
            poly_term += x[i]**6 + 0.7 * x[i]**5 - 0.4 * x[i]**4 + 0.2 * x[i]**3
        result += 1.5 * poly_term * np.sin(8 * np.sum(x))
        
        # Cross-dimensional exponential interaction with multiple sine couplings and dynamic scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.9 * np.exp(-np.abs(x[i] - x[j]) / (1 + 0.4 * np.abs(x[i] + x[j]))) * np.cos(15 * (x[i] - x[j])) * (1 + 0.2 * np.sin(13 * (x[i] + x[j])))
        
        # Additional asymmetric wave pattern with hyperbolic tangent and chaotic modulation
        sum_x = np.sum(x)
        result += 2.5 * np.sin(35 * sum_x) * np.cos(30 * sum_x) * (1 + 0.6 * np.tanh(3 * sum_x)) * (1 + 0.4 * np.sin(27 * sum_x))
        
        # Cross-dimensional polynomial coupling with septic terms and chaotic sine modulation
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                result += 0.7 * (x[i]**4 + x[j]**4) * np.sin(6 * (x[i] - x[j])) * (1 + 0.3 * np.cos(22 * x[i]))
        
        # Additional high-frequency noise component with chaotic sine and cosine
        noise = 0.0
        for i in range(self.dim):
            noise += 0.4 * np.sin(60 * x[i]) * np.cos(55 * x[i]) + 0.2 * np.cos(65 * x[i]) * np.sin(50 * x[i])
        result += noise
        
        # Improved conditioning and separation through modified exponential terms with chaotic phases
        for i in range(self.dim):
            result += 1.1 * np.exp(-0.4 * (x[i] - 1.8)**2) * np.sin(25 * x[i]) * np.cos(20 * x[i]) * (1 + 0.3 * np.sin(18 * x[i]))
        
        # Additional dimension coupling with sine modulation, exponential decay, and chaotic offsets
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.8 * np.sin(9 * (x[i] + x[j])) * np.exp(-0.25 * (x[i] - x[j])**2) * (1 + 0.4 * np.cos(11 * x[i]) + 0.2 * np.sin(14 * x[j]))
        
        # Enhanced global structure with weighted harmonic components and chaotic modulation
        harmonic_sum = 0
        for i in range(self.dim):
            harmonic_sum += np.sin(6 * x[i]) * np.cos(5 * x[i]) * np.exp(-0.15 * x[i]**2) * (1 + 0.2 * np.sin(17 * x[i]))
        result += 1.7 * harmonic_sum**2
        
        # Additional complex cross-dimensional interactions with higher-order polynomial terms
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                for k in range(j+1, min(j+4, self.dim)):
                    result += 0.5 * (x[i]**3 + x[j]**3 + x[k]**3) * np.cos(8 * (x[i] - x[j] + x[k])) * np.sin(7 * (x[i] + x[j] - x[k]))
        
        # Additional chaotic modulation with recursive sine and cosine terms
        chaos_mod = 0.0
        for i in range(self.dim):
            chaos_mod += np.sin(31 * x[i]) * np.cos(29 * x[i]) * np.sin(37 * x[i]**2) * np.cos(33 * x[i]**3)
        result += 1.4 * chaos_mod
        
        # Enhanced fractal-like structure with nested trigonometric and polynomial components
        fractal_sum = 0.0
        for i in range(self.dim):
            fractal_sum += np.sin(40 * x[i]) * np.cos(35 * x[i]) * np.sin(28 * x[i]**2) * (1 + 0.3 * np.abs(x[i]))
        result += 2.1 * fractal_sum**2
        
        # Additional multi-scale interaction terms with dynamic weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale_factor = 1.0 + 0.2 * np.sin(25 * (x[i] - x[j]))
                result += 0.6 * np.exp(-0.3 * (x[i] - x[j])**2) * np.cos(10 * (x[i] + x[j])) * scale_factor
        
        return result