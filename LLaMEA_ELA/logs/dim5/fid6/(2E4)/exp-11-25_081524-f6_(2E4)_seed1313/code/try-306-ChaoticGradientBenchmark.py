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
            chaos_factor = 1.0 + 0.9 * np.sin(5.0 * self.t + i * 1.8) * np.cos(2.5 * self.t)
            result += (xi**2 - 4.0 * xi + 4.0) * chaos_factor
            
        # Improved periodic attractor landscape with stronger frequency coupling and more harmonics
        freq_mod = 1.0 + 0.8 * np.sin(2.0 * self.t)  # Increased modulation
        for i in range(self.dim):
            xi = x[i]
            result += 1.5 * (xi**2) * np.cos(freq_mod * xi + 0.7 * self.t)
            
        # Enhanced dynamic curvature with stronger time-varying effects and additional terms
        curv_factor = 1.0 + 0.9 * np.sin(3.0 * self.t)  # Increased variation
        for i in range(self.dim):
            xi = x[i]
            result += curv_factor * (xi**3 - 3.0 * xi) * np.exp(-xi**2/1.5)
            
        # Strengthened saddle point configuration with more complex coupling and additional interactions
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                xi = x[i]
                xj = x[i+1]
                result += 1.0 * (xi**2 - xj**2) * np.sin(1.3 * (xi + xj))  # Increased coupling
                
        # Enhanced multi-scale periodicity with stronger phase coupling and additional frequencies
        for i in range(self.dim):
            xi = x[i]
            result += 0.8 * np.sin(20.0 * xi + 0.3 * self.t) * np.cos(8.0 * xi + 0.4 * self.t)  # Increased frequencies
            
        # Refined basin depth with more controlled scaling and additional polynomial terms
        scale_factor = 2.0 + 1.2 * np.sin(1.3 * self.t)  # Increased variation
        result += scale_factor * np.sum((x**4) * np.exp(-x**2/0.8))
        
        # Enhanced coupled logistic dynamics in the landscape with increased nonlinearity
        for i in range(self.dim):
            xi = x[i]
            logistic_val = self.logistic_r * xi * (1.0 - xi)
            result += 0.25 * logistic_val * np.sin(4.0 * xi + 0.7 * self.t)  # Increased nonlinearity
            
        # Strengthened oscillating harmonic components with higher frequencies
        for i in range(self.dim):
            xi = x[i]
            result += 0.5 * (xi**2) * np.sin(15.0 * xi + 0.6 * self.t) * np.cos(7.0 * xi + 0.4 * self.t)  # Increased frequencies
            
        # Additional harmonic interference terms for increased complexity with higher frequency components
        for i in range(self.dim):
            xi = x[i]
            result += 0.22 * np.sin(8.5 * xi + 0.4 * self.t) * np.cos(4.0 * xi + 0.3 * self.t)  # Increased frequencies
            
        # Mutation: Slight adjustment to curvature and interaction terms with increased complexity
        for i in range(self.dim):
            xi = x[i]
            result += 0.15 * (xi**4 - 2*xi**2) * np.sin(5.0 * xi + 0.3 * self.t)  # Increased complexity
            
        # Mutation: Reduced coupling strength in harmonic interference with additional nonlinear components
        for i in range(self.dim):
            xi = x[i]
            result += 0.18 * np.sin(7.0 * xi + 0.4 * self.t) * np.cos(3.0 * xi + 0.3 * self.t)  # Increased frequencies
            
        # Additional chaotic interference terms with more complex interactions
        for i in range(self.dim):
            xi = x[i]
            result += 0.22 * np.sin(25.0 * xi + 0.4 * self.t) * np.cos(10.0 * xi + 0.3 * self.t)  # Increased frequencies
            
        # Enhanced multi-modal structure with stronger local minima and higher order polynomial terms
        for i in range(self.dim):
            xi = x[i]
            result += 0.4 * (xi**6 - 3*xi**4 + 3*xi**2) * np.exp(-xi**2/3.0)  # Increased complexity
            
        # Increased dimensionality coupling with cross-terms and higher order interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                result += 0.12 * (xi**2 + xj**2) * np.sin(0.5 * (xi - xj))  # Increased coupling strength
                
        # Additional high-frequency chaotic components for enhanced difficulty
        for i in range(self.dim):
            xi = x[i]
            result += 0.15 * np.sin(35.0 * xi + 0.5 * self.t) * np.cos(15.0 * xi + 0.4 * self.t)  # Extremely high frequencies
            
        # Increased complexity through higher-order polynomial interactions
        for i in range(self.dim):
            xi = x[i]
            result += 0.08 * (xi**5 - 2*xi**3 + xi) * np.exp(-xi**2/4.0)
            
        # Novel higher-order polynomial interactions for extreme complexity
        for i in range(self.dim):
            xi = x[i]
            result += 0.1 * (xi**7 - 4*xi**5 + 6*xi**3 - 4*xi) * np.exp(-xi**2/2.5)
            
        # Cross-dimensional higher-order coupling terms with altered exponents
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                result += 0.05 * (xi**3 * xj**2 + xi**2 * xj**3) * np.sin(0.3 * (xi + xj))
                
        # Additional chaotic sine-cosine combinations for maximum interference
        for i in range(self.dim):
            xi = x[i]
            result += 0.12 * np.sin(40.0 * xi + 0.55 * self.t) * np.cos(18.0 * xi + 0.45 * self.t)
            
        # Enhanced non-linear exponential coupling with time-varying parameters
        for i in range(self.dim):
            xi = x[i]
            result += 0.06 * (xi**2) * np.exp(-xi**2/3.0) * np.sin(2.5 * self.t + xi)
            
        # Mutation: Changed polynomial exponents and coupling strengths to increase landscape ruggedness
        for i in range(self.dim):
            xi = x[i]
            result += 0.18 * (xi**5 - 2*xi**3 + xi**2) * np.exp(-xi**2/2.0)  # Modified exponents
            
        # Mutation: Altered coupling coefficients and harmonic frequencies for more challenging search
        for i in range(self.dim):
            xi = x[i]
            result += 0.25 * (xi**3) * np.sin(18.0 * xi + 0.4 * self.t) * np.cos(9.0 * xi + 0.3 * self.t)
            
        # Mutation: Adjusted interaction terms to increase local minima density
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                result += 0.15 * (xi**2 + xj**3) * np.sin(0.4 * (xi - xj))  # Altered coupling
                
        return result