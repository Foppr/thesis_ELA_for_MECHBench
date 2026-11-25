import numpy as np

class RadialLogisticSkewLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Radial basis function centers and widths
        self.centers = np.random.uniform(-4.0, 4.0, (dim, 10))
        self.widths = 0.5 + 2.0 * np.random.rand(10)
        # Logistic map parameters for chaotic behavior
        self.logistic_r = 3.9 + 0.1 * np.random.rand(dim)
        self.logistic_x = 0.5 + 0.1 * np.random.rand(dim)
        # Adaptive skewness parameters
        self.skew_params = np.random.uniform(0.5, 2.0, dim)
        self.skew_shifts = np.random.uniform(-1.0, 1.0, dim)
        # Cross-dimensional coupling with exponential decay
        self.coupling_strength = 0.3 + 0.4 * np.random.rand(dim, dim)
        # Dimensional conditioning factors
        self.conditioning = 1.0 + 0.5 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function component
        rbf_sum = 0.0
        for i in range(10):
            dist = np.sum((x_norm[:, None] - self.centers[:, i])**2, axis=0)
            rbf_sum += np.exp(-self.widths[i] * dist)
        
        # Logistic map chaotic component
        logistic_sum = 0.0
        for i in range(self.dim):
            # Update logistic map
            self.logistic_x[i] = self.logistic_r[i] * self.logistic_x[i] * (1 - self.logistic_x[i])
            logistic_sum += self.logistic_x[i] * np.sin(x_norm[i])
        
        # Adaptive skewness transformation
        skew_sum = 0.0
        for i in range(self.dim):
            skewed_x = (x_norm[i] - self.skew_shifts[i]) ** self.skew_params[i]
            skew_sum += skewed_x * np.cos(x_norm[i])
        
        # Cross-dimensional coupling with exponential decay
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = self.coupling_strength[i, j] * np.exp(-0.5 * (x_norm[i]**2 + x_norm[j]**2))
                    coupling_sum += coupling * np.sin(x_norm[i] * x_norm[j])
        
        # Combined landscape
        result = 0.4 * rbf_sum + 0.3 * logistic_sum + 0.2 * skew_sum + 0.1 * coupling_sum
        
        # Dimensional conditioning and penalty
        condition_factor = np.prod(self.conditioning)
        penalty = 0.1 * np.sum(x_norm**6)
        
        return result * condition_factor + penalty + 0.05 * np.sum(np.abs(x_norm)**8)