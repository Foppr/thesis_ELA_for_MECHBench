import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Base quadratic term with strong conditioning
        f = np.sum(x**2) * 0.8
        
        # Add chaotic sinusoidal grid pattern with high-frequency interactions
        for i in range(self.dim):
            f += 0.4 * np.sin(13 * x[i]) * np.cos(11 * x[i]) * np.sin(7 * x[i])
            
        # Add nested multi-scale interactions with exponential coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):  # Extended range for complexity
                f += 0.2 * np.sin(5 * x[i] + 4 * x[j]) * np.cos(9 * x[i] - 3 * x[j]) * np.sin(3 * x[i] + 2 * x[j])
                
        # Add fractal-like self-similar structure with recursive pattern
        for i in range(self.dim):
            f += 0.1 * np.sin(17 * np.sin(5 * x[i])) * np.cos(12 * np.cos(4 * x[i])) * np.sin(8 * np.sin(3 * x[i]))
            
        # Add higher-order polynomial interactions with non-linear coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, min(j+5, self.dim)):
                    f += 0.05 * x[i]**4 * np.sin(x[j] + x[k]) * np.cos(x[i] * x[j])
                    
        # Add multiple global minima at non-origin locations with varying scales
        global_minima = np.array([[-3.0, 3.0], [3.0, -3.0], [-3.0, -3.0], [3.0, 3.0], 
                                 [-1.5, 1.5], [1.5, -1.5], [-1.5, -1.5], [1.5, 1.5],
                                 [-4.0, 2.0], [2.0, -4.0], [-2.0, -4.0], [4.0, 2.0],
                                 [-2.5, 2.5], [2.5, -2.5], [-3.5, 3.5], [3.5, -3.5],
                                 [-1.0, 1.0], [1.0, -1.0], [-4.5, 4.5], [4.5, -4.5]])
        if self.dim >= 2:
            minima_term = 0
            for min_point in global_minima:
                if self.dim >= len(min_point):
                    diff = x[:len(min_point)] - min_point
                    minima_term += np.exp(-0.4 * np.sum(diff**2))
            f += 0.5 * minima_term
            
        # Add noise component with non-uniform distribution for additional challenge
        f += 0.03 * np.sum(np.sin(17 * x)**2 + np.cos(10 * x)**2)
        
        # Add dimensional coupling with cross-terms that increase complexity exponentially
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f += 0.07 * np.sin(3 * x[i] * x[j]) * np.cos(4 * x[i] + x[j]) * np.sin(x[i] - x[j])
                
        # Add chaotic phase modulation for increased non-linearity
        phase_mod = 0
        for i in range(self.dim):
            phase_mod += np.sin(2 * np.pi * x[i] * (i + 1) * 0.15)
        f += 0.15 * np.sin(phase_mod)
        
        # Add additional chaotic modulation with recursive structure
        for i in range(self.dim):
            f += 0.06 * np.sin(20 * np.sin(6 * x[i])) * np.cos(15 * np.cos(5 * x[i]))
            
        # Add enhanced dimensional coupling with trigonometric polynomial terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f += 0.04 * np.sin(4 * x[i] * x[j] + x[i] + x[j]) * np.cos(5 * x[i] - x[j]) * np.sin(2 * x[i] * x[j])
                
        # Add additional complex interaction terms for increased challenge
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    f += 0.03 * np.sin(2 * x[i] + 3 * x[j] - x[k]) * np.cos(x[i] * x[j] * x[k]) * np.sin(x[i] - x[j] + x[k])
                    
        # Add higher-order chaotic interactions with more complex coupling
        for i in range(self.dim):
            f += 0.08 * np.sin(25 * np.sin(7 * x[i])) * np.cos(20 * np.cos(6 * x[i])) * np.sin(15 * np.sin(5 * x[i]))
            
        # Add non-uniform scaling and additional chaotic modulation
        for i in range(self.dim):
            f += 0.02 * np.sin(30 * x[i]**3) * np.cos(25 * x[i]**2) * np.sin(20 * x[i])
            
        # Add large-scale chaotic modulation with variable frequency
        for i in range(self.dim):
            f += 0.1 * np.sin(35 * np.sin(8 * x[i])) * np.cos(30 * np.cos(7 * x[i])) * np.sin(25 * np.sin(6 * x[i]))
            
        # Add ultra-high frequency chaotic sinusoidal components
        for i in range(self.dim):
            f += 0.05 * np.sin(50 * x[i]) * np.cos(45 * x[i]) * np.sin(40 * x[i])
            
        # Add multi-scale nested global minima with irregular spacing
        irregular_minima = np.array([[-4.2, 3.8], [3.8, -4.2], [-3.7, -3.7], [3.7, 3.7],
                                    [-2.8, 2.8], [2.8, -2.8], [-4.8, 1.2], [1.2, -4.8],
                                    [-1.2, -4.8], [4.8, 1.2], [-3.2, 3.2], [3.2, -3.2],
                                    [-2.1, 4.9], [4.9, -2.1], [-4.9, 2.1], [2.1, -4.9]])
        if self.dim >= 2:
            irregular_term = 0
            for min_point in irregular_minima:
                if self.dim >= len(min_point):
                    diff = x[:len(min_point)] - min_point
                    irregular_term += np.exp(-0.3 * np.sum(diff**2))
            f += 0.6 * irregular_term
            
        # Add enhanced dimensional coupling with non-linear scaling factors
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f += 0.09 * np.sin(6 * x[i] * x[j]) * np.cos(7 * x[i] + 2 * x[j]) * np.sin(5 * x[i] - 3 * x[j]) * np.cos(4 * x[i] * x[j])
                
        # Add ultra-complex interaction terms with 4th-order coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    for l in range(k+1, min(k+4, self.dim)):
                        f += 0.02 * np.sin(3 * x[i] + 2 * x[j] - x[k] + x[l]) * np.cos(x[i] * x[j] * x[k] * x[l]) * np.sin(x[i] - x[j] + x[k] - x[l])
                        
        # Mutation: Slightly increase the influence of higher-order terms and add new interaction
        for i in range(self.dim):
            f += 0.1 * np.sin(35 * x[i]**2) * np.cos(30 * x[i]) * np.sin(25 * x[i]**3)
            
        # Add new chaotic interaction term with 5th-order coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    for l in range(k+1, self.dim):
                        for m in range(l+1, min(l+3, self.dim)):
                            f += 0.015 * np.sin(2 * x[i] + x[j] - x[k] + x[l] - x[m]) * np.cos(x[i] * x[j] * x[k] * x[l] * x[m]) * np.sin(x[i] - x[j] + x[k] - x[l] + x[m])
                            
        return f