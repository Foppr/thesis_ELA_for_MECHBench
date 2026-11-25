import numpy as np

class QuaternionHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrices for quaternion-inspired symmetries
        self.rotations = []
        for i in range(4):
            angle = i * np.pi / 2.0
            rot = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
            self.rotations.append(rot)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with Gaussian kernels
        rbf_term = 0.0
        centers = np.random.uniform(-4.0, 4.0, (10, self.dim))
        for i in range(10):
            dist = np.linalg.norm(x - centers[i])
            rbf_term += np.exp(-0.5 * dist**2 / 4.0)
        
        # Quaternion-inspired rotational symmetry component
        rot_symmetry = 0.0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                # Apply 2D rotation matrix to pairs of dimensions
                pair = x[i:i+2]
                rotated = np.dot(self.rotations[0], pair)
                rot_symmetry += np.sum(rotated**2)
        
        # Temporal harmonic coupling with time-varying frequencies
        temporal_coupling = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.1 * i)
            temporal_coupling += np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        
        # Nested valley structure with multiple local minima
        valley_term = 0.0
        for i in range(self.dim):
            valley_term += (x[i]**2 - 10 * np.cos(0.5 * x[i]))**2
        
        # Cross-dimensional coupling with exponential interaction weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.1 * (i - j)**2)
                cross_coupling += weight * np.sin(x[i] + x[j])
        
        # Asymmetric landscape with piecewise polynomial terms
        asym_term = 0.0
        for i in range(self.dim):
            if x[i] >= 0:
                asym_term += x[i]**3 + 0.5 * x[i]**2
            else:
                asym_term += x[i]**4 - 0.3 * x[i]**2
        
        # Combine all terms with adaptive weights
        total = 0.25 * rbf_term + 0.20 * rot_symmetry + 0.18 * temporal_coupling + 0.15 * valley_term + 0.12 * cross_coupling + 0.10 * asym_term
        
        return total