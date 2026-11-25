import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        self.logistic_r = 3.9 + 0.1 * np.sin(0.5 * self.t)
        
    def f(self, x):
        self.t += 0.01
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient components with logistic map dynamics
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced chaotic modulation with stronger coupling and higher frequency
            chaos_factor = 1.0 + 0.8 * np.sin(4.0 * self.t + i * 1.5) * np.cos(2.0 * self.t)
            result += (xi**2 - 4.0 * xi + 4.0) * chaos_factor
            
        # Improved periodic attractor landscape with stronger frequency coupling and more harmonics
        freq_mod = 1.0 + 0.7 * np.sin(1.5 * self.t)  # Increased modulation
        for i in range(self.dim):
            xi = x[i]
            result += 1.2 * (xi**2) * np.cos(freq_mod * xi + 0.6 * self.t)
            
        # Enhanced dynamic curvature with stronger time-varying effects and additional terms
        curv_factor = 1.0 + 0.8 * np.sin(2.5 * self.t)  # Increased variation
        for i in range(self.dim):
            xi = x[i]
            result += curv_factor * (xi**3 - 3.0 * xi) * np.exp(-xi**2/2.0)
            
        # Strengthened saddle point configuration with more complex coupling and additional interactions
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                xi = x[i]
                xj = x[i+1]
                result += 0.8 * (xi**2 - xj**2) * np.sin(1.1 * (xi + xj))  # Increased coupling
                
        # Enhanced multi-scale periodicity with stronger phase coupling and additional frequencies
        for i in range(self.dim):
            xi = x[i]
            result += 0.7 * np.sin(16.0 * xi + 0.25 * self.t) * np.cos(6.0 * xi + 0.35 * self.t)  # Increased frequencies
            
        # Refined basin depth with more controlled scaling and additional polynomial terms
        scale_factor = 1.8 + 1.0 * np.sin(1.1 * self.t)  # Increased variation
        result += scale_factor * np.sum((x**4) * np.exp(-x**2/1.0))
        
        # Enhanced coupled logistic dynamics in the landscape with increased nonlinearity
        for i in range(self.dim):
            xi = x[i]
            logistic_val = self.logistic_r * xi * (1.0 - xi)
            result += 0.2 * logistic_val * np.sin(3.5 * xi + 0.6 * self.t)  # Increased nonlinearity
            
        # Strengthened oscillating harmonic components with higher frequencies
        for i in range(self.dim):
            xi = x[i]
            result += 0.4 * (xi**2) * np.sin(12.0 * xi + 0.5 * self.t) * np.cos(6.0 * xi + 0.3 * self.t)  # Increased frequencies
            
        # Additional harmonic interference terms for increased complexity with higher frequency components
        for i in range(self.dim):
            xi = x[i]
            result += 0.18 * np.sin(7.5 * xi + 0.3 * self.t) * np.cos(3.2 * xi + 0.2 * self.t)  # Increased frequencies
            
        # Mutation: Slight adjustment to curvature and interaction terms with increased complexity
        for i in range(self.dim):
            xi = x[i]
            result += 0.12 * (xi**4 - 2*xi**2) * np.sin(4.0 * xi + 0.2 * self.t)  # Increased complexity
            
        # Mutation: Reduced coupling strength in harmonic interference with additional nonlinear components
        for i in range(self.dim):
            xi = x[i]
            result += 0.15 * np.sin(6.0 * xi + 0.3 * self.t) * np.cos(2.5 * xi + 0.2 * self.t)  # Increased frequencies
            
        # Additional chaotic interference terms with more complex interactions
        for i in range(self.dim):
            xi = x[i]
            result += 0.18 * np.sin(22.0 * xi + 0.35 * self.t) * np.cos(9.0 * xi + 0.25 * self.t)  # Increased frequencies
            
        # Enhanced multi-modal structure with stronger local minima and higher order polynomial terms
        for i in range(self.dim):
            xi = x[i]
            result += 0.35 * (xi**6 - 3*xi**4 + 3*xi**2) * np.exp(-xi**2/3.8)  # Increased complexity
            
        # Increased dimensionality coupling with cross-terms and higher order interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                result += 0.08 * (xi**2 + xj**2) * np.sin(0.4 * (xi - xj))  # Increased coupling strength
                
        # Additional high-frequency chaotic components for enhanced difficulty
        for i in range(self.dim):
            xi = x[i]
            result += 0.1 * np.sin(30.0 * xi + 0.4 * self.t) * np.cos(12.0 * xi + 0.3 * self.t)  # Extremely high frequencies
            
        # Increased complexity through higher-order polynomial interactions
        for i in range(self.dim):
            xi = x[i]
            result += 0.05 * (xi**5 - 2*xi**3 + xi) * np.exp(-xi**2/5.0)
            
        # Mutation: Adjusted coupling strengths and harmonic frequencies to create a more challenging landscape
        for i in range(self.dim):
            xi = x[i]
            result += 0.14 * (xi**2 - 2*xi + 1) * np.sin(5.0 * xi + 0.2 * self.t)  # Increased coupling
            
        # Mutation: Additional cross-dimensional interaction with modified frequency
        for i in range(0, self.dim, 3):
            if i + 2 < self.dim:
                xi = x[i]
                xj = x[i+1]
                xk = x[i+2]
                result += 0.06 * (xi**2 + xj**2 - xk**2) * np.cos(0.5 * (xi + xj + xk))  # Modified coupling
                
        return result