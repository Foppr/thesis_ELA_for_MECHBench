import numpy as np

class RadialSaddleNoiseLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 10)
        # Initialize saddle points with varying heights and orientations
        self.saddle_points = np.random.uniform(-5.0, 5.0, (5, dim))
        self.saddle_heights = np.random.uniform(-2.0, 2.0, 5)
        self.saddle_orientations = np.random.uniform(0, 2*np.pi, 5)
        # Initialize noise parameters
        self.noise_amplitude = np.random.uniform(0.1, 0.5, dim)
        self.noise_frequency = np.random.uniform(0.5, 2.0, dim)
        # Initialize adaptive scaling factors
        self.scaling_factors = np.random.uniform(0.5, 1.5, dim)
        # Initialize correlation coefficients between dimensions
        self.correlation_matrix = np.random.uniform(-0.3, 0.3, (dim, dim))
        np.fill_diagonal(self.correlation_matrix, 1.0)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute radial basis function components
        rbf_terms = 0.0
        for i in range(10):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            rbf_term = np.exp(-np.sum(((x - center) / width) ** 2))
            rbf_terms += rbf_term
        
        # Compute saddle point components
        saddle_terms = 0.0
        for i in range(5):
            point = self.saddle_points[i]
            height = self.saddle_heights[i]
            orientation = self.saddle_orientations[i]
            dx = x - point
            # Create rotated saddle structure
            rotated_dx = np.array([dx[0] * np.cos(orientation) + dx[1] * np.sin(orientation),
                                  -dx[0] * np.sin(orientation) + dx[1] * np.cos(orientation)])
            saddle_term = height * (rotated_dx[0]**2 - rotated_dx[1]**2)
            saddle_terms += saddle_term
        
        # Compute noise injection components
        noise_terms = 0.0
        for j in range(self.dim):
            noise_term = self.noise_amplitude[j] * np.sin(self.noise_frequency[j] * x[j])
            noise_terms += noise_term
        
        # Apply adaptive scaling
        scale_terms = 0.0
        for j in range(self.dim):
            scale_term = self.scaling_factors[j] * x[j]**3
            scale_terms += scale_term
        
        # Compute correlation effects
        corr_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    corr_terms += self.correlation_matrix[i, j] * x[i] * x[j]
        
        # Combine all components with appropriate weights
        total = 0.3 * rbf_terms + 0.4 * saddle_terms + 0.2 * noise_terms + 0.1 * scale_terms + 0.05 * corr_terms
        
        return total