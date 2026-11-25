import numpy as np

class RotatedHyperEllipsoidBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize rotation matrices for each dimension
        self.rotation_matrices = []
        for i in range(dim):
            # Generate random orthogonal matrices
            A = np.random.randn(i+1, i+1)
            Q, _ = np.linalg.qr(A)
            self.rotation_matrices.append(Q)
        
        # Adaptive conditioning parameters
        self.conditioning = np.random.uniform(1.0, 100.0, dim)
        
        # Non-linear coupling weights
        self.coupling_weights = np.random.uniform(-0.5, 0.5, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Apply rotation and conditioning
        rotated_x = x_norm.copy()
        for i in range(self.dim):
            if i > 0:
                rotated_x[:i+1] = self.rotation_matrices[i].dot(x_norm[:i+1])
        
        # Hyper-ellipsoid terms with adaptive conditioning
        hyper_ellipse = 0.0
        for i in range(self.dim):
            term = self.conditioning[i] * (rotated_x[i]**2)
            if i > 0:
                term += np.sum([self.coupling_weights[j] * rotated_x[j] * rotated_x[i] 
                               for j in range(i)])
            hyper_ellipse += term
        
        # Add non-linear coupling and interaction terms
        nonlinear_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Non-linear interaction between dimensions
                interaction = np.sin(rotated_x[i]) * np.cos(rotated_x[j]) + \
                              np.exp(-0.5 * (rotated_x[i] - rotated_x[j])**2)
                nonlinear_coupling += interaction
        
        # Add noise and scaling for increased complexity
        noise = np.random.normal(0, 0.1)
        
        return hyper_ellipse + 0.5 * nonlinear_coupling + noise