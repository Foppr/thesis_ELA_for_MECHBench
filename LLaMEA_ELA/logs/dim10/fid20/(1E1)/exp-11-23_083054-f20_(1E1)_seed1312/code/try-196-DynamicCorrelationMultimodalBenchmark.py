import numpy as np

class DynamicCorrelationMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Dynamic correlation matrix with varying strengths
        self.correlation_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                if i == j:
                    self.correlation_matrix[i, j] = 1.0
                else:
                    # Varying correlation strengths based on position
                    strength = 0.3 + 0.4 * np.sin(0.5 * (i + j)) * np.cos(0.3 * (i - j))
                    self.correlation_matrix[i, j] = strength
        
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-3.0, 3.0, (dim, 5))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 5)
        
        # Polynomial coefficients with varying degrees
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Sinusoidal component with dynamic frequencies
        f1 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * i) + 0.8 * np.cos(0.4 * i)
            amp = 1.0 + 0.5 * np.sin(0.6 * i)
            phase = 0.5 * np.cos(0.7 * i)
            f1 += amp * np.sin(freq * x_norm[i] + phase) * np.exp(-0.2 * x_norm[i]**2)
        
        # Radial basis function component
        f2 = 0.0
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(5):
                dist = np.sum((x_norm[i] - self.rbf_centers[i, j])**2)
                rbf_sum += self.rbf_widths[j] * np.exp(-dist / (2.0 * self.rbf_widths[j]**2))
            f2 += rbf_sum
        
        # Polynomial component with mixed terms
        f3 = 0.0
        for i in range(self.dim):
            poly_term = 0.0
            for deg in range(1, 5):
                poly_term += self.poly_coeffs[i] * (x_norm[i]**deg)
            f3 += poly_term
        
        # Cross-term correlations with dynamic weights
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr_weight = self.correlation_matrix[i, j]
                cross_term = x_norm[i] * x_norm[j] * np.sin(2.0 * (x_norm[i] + x_norm[j]))
                f4 += corr_weight * cross_term
        
        # Mixed exponential and trigonometric with dynamic scaling
        f5 = 0.0
        for i in range(self.dim):
            exp_part = np.exp(-0.1 * np.abs(x_norm[i]))
            trig_part = np.sin(3.0 * x_norm[i]) + 0.7 * np.cos(2.5 * x_norm[i])
            scale = 1.0 + 0.3 * np.sin(0.8 * i)
            f5 += exp_part * trig_part * scale
        
        # Combine all components with dynamic weights
        total = 0.0
        weights = [0.2 + 0.1 * np.sin(0.4 * i) for i in range(5)]
        
        # Apply different combinations based on input position
        pos_factor = np.sum(x_norm**2) / self.dim
        if pos_factor < 0.5:
            total = weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4 + weights[4] * f5
        else:
            total = weights[1] * f1 + weights[0] * f2 + weights[3] * f3 + weights[2] * f4 + weights[4] * f5
            
        return total