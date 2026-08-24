import numpy as np

class RadialPeriodicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis centers and widths
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.widths = np.random.uniform(0.5, 2.0, 10)
        self.amplitudes = np.random.uniform(1.0, 3.0, 10)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component
        rbf = 0.0
        for i in range(10):
            distance = np.sum((x - self.centers[i])**2)
            rbf += self.amplitudes[i] * np.exp(-self.widths[i] * distance)
        
        # Periodic oscillation component with varying frequencies
        period_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.5)
            period_term += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        
        # Adaptive conditioning based on variable magnitude
        cond_term = 0.0
        for i in range(self.dim):
            cond_term += (1.0 + 0.5 * np.abs(x[i])) * x[i]**2
        
        # Coupled sine waves with phase interactions
        phase_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_coupling += np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Asymmetric penalty for boundary proximity
        boundary_penalty = 0.0
        for i in range(self.dim):
            boundary_penalty += 10.0 * (np.abs(x[i]) - 5.0)**2 * (x[i] > 4.5)
        
        # Combine all components
        result = rbf + 0.5 * period_term + 0.3 * cond_term + 0.2 * phase_coupling + boundary_penalty
        
        return result