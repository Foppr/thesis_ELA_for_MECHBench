import numpy as np

class QuaternionPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quaternion-based rotational parameters
        self.quat_axes = np.random.randn(dim, 3)
        self.quat_angles = np.random.uniform(0, 2*np.pi, dim)
        self.rotation_matrices = []
        for i in range(dim):
            ax = self.quat_axes[i]
            ax = ax / np.linalg.norm(ax)
            angle = self.quat_angles[i]
            # Generate rotation matrix from axis-angle
            cos_a = np.cos(angle)
            sin_a = np.sin(angle)
            xx, xy, xz = ax[0]*ax[0], ax[0]*ax[1], ax[0]*ax[2]
            yy, yz, zz = ax[1]*ax[1], ax[1]*ax[2], ax[2]*ax[2]
            self.rotation_matrices.append(np.array([
                [cos_a + (1-cos_a)*(xx), (1-cos_a)*xy - sin_a*ax[2], (1-cos_a)*xz + sin_a*ax[1]],
                [(1-cos_a)*xy + sin_a*ax[2], cos_a + (1-cos_a)*(yy), (1-cos_a)*yz - sin_a*ax[0]],
                [(1-cos_a)*xz - sin_a*ax[1], (1-cos_a)*yz + sin_a*ax[0], cos_a + (1-cos_a)*(zz)]
            ]))
        
        # Polynomial chaos expansion coefficients
        self.poly_coeffs = np.random.randn(dim, 6)
        
        # Adaptive penalty parameters
        self.penalty_centers = np.random.uniform(-4.8, 4.8, (dim, 5))
        self.penalty_weights = np.random.uniform(0.5, 3.0, (dim, 5))
        self.penalty_widths = np.random.uniform(0.2, 1.5, (dim, 5))
        
        # Gradient discontinuity locations
        self.discontinuities = np.random.uniform(-4.8, 4.8, (dim, 4))
        
    def f(self, x):
        x = np.array(x)
        
        # Quaternion-based rotational component
        rot_term = 0.0
        for i in range(self.dim):
            # Apply rotation to x[i]
            rotated_x = np.dot(self.rotation_matrices[i], np.array([x[i], 0, 0]))
            rot_term += rotated_x[0] * np.sin(x[i]) + rotated_x[1] * np.cos(x[i])
        
        # Polynomial chaos expansion component
        poly_term = 0.0
        for i in range(self.dim):
            coeffs = self.poly_coeffs[i]
            x_i = x[i]
            poly_term += coeffs[0] + coeffs[1]*x_i + coeffs[2]*x_i**2 + coeffs[3]*x_i**3 + \
                         coeffs[4]*x_i**4 + coeffs[5]*x_i**5
        
        # Adaptive penalty landscape
        penalty_term = 0.0
        for i in range(self.dim):
            for j in range(5):
                center = self.penalty_centers[i, j]
                weight = self.penalty_weights[i, j]
                width = self.penalty_widths[i, j]
                penalty_term += weight * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Gradient discontinuity term
        grad_discont = 0.0
        for i in range(self.dim):
            for j in range(4):
                if abs(x[i] - self.discontinuities[i, j]) < 0.1:
                    grad_discont += 10.0 * np.sin(x[i])
        
        # Coupling between dimensions through rotational interactions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += (x[i] * x[j]) * np.sin(np.sum(x[:min(i,j)+1]))
        
        # Global scaling and symmetry breaking
        total = 0.25 * rot_term + 0.30 * poly_term + 0.25 * penalty_term + \
                0.15 * grad_discont + 0.05 * coupling_term
        
        # Add non-smoothness through a fractal-like transformation
        fractal_mod = np.prod([np.sin(x[i] * (i+1)) for i in range(self.dim)])
        
        return total * (1.0 + 0.3 * fractal_mod)